import sys
import json


def snake_case_to_camel_case(string, is_lower=False):
    if is_lower:
        string_to_check = string.split('_')
        return string_to_check[0] + ''.join(word.title() for word in string_to_check[1:])
    else:
        return ''.join(word.title() for word in string.split('_'))


def remove_spaces(line):
    return line.replace(" ", "")


def remove_next_lines(line):
    return line.replace("\n", "")


def remove_next_tabs(line):
    return line.replace("\t", "")


def remove_all_imports(f):
    classes_lines = ""
    for line in f.readlines():
        line = remove_spaces(line)
        line = remove_next_lines(line)
        line = remove_next_tabs(line)
        if not line.startswith("return") and not line.startswith("def") and not line.startswith(
                "import") and not line.startswith("from") and not len(line.strip()) == 0:
            classes_lines = classes_lines + line
    return classes_lines


def add_imports():
    import1 = "import {Model} from \'@nozbe/watermelondb\' \n"
    import2 = "import {action, field, date, relation} from \'@nozbe/watermelondb/decorators\' \n"
    return import1 + import2


def add_quotes(string):
    string = string.replace("name:", "\"name\":")
    string = string.replace("type:", "\"type\":")
    string = string.replace("tables:", "\"tables\":")
    string = string.replace("columns:", "\"columns\":")
    string = string.replace("version:", "\"version\":")
    string = string.replace("\'", "\"")
    string = string.replace("},]", "}]")
    string = string.replace("],}", "]}")
    return string


def get_the_app_schema(data):
    index = data.index("(")
    data = data[index + 1:-1]
    data = data.replace("tableSchema", "")
    data = data.replace("(", "")
    data = data.replace(")", "")
    return data


def get_tables_json_data(f):
    data = remove_all_imports(f)
    data = get_the_app_schema(data)
    data = add_quotes(data)
    data = json.loads(data)
    return data


def prepare_model_name(string):
    string = snake_case_to_camel_case(string, False)
    if string.endswith("s"):
        string = string[:-1]
    return string


def prepare_class_line(string):
    return "class " + prepare_model_name(string) + " extends Model { \n \n"


def prepare_export_line(string):
    string = snake_case_to_camel_case(string, False)
    if string.endswith("s"):
        string = string[:-1]
    return "export default " + string + " \n \n"


def prepare_table_line(string):
    return "    static table = \'" + string + "\' \n \n"


def get_decorator(name):
    camelName = snake_case_to_camel_case(name, True)
    if name.endswith("_id"):
        parent_table_name = name.replace("_id", "")
        if str(parent_table_name).endswith("s"):
            parent_table_name = parent_table_name
        else:
            parent_table_name = parent_table_name + "s"
        return "    @relation(\'" + parent_table_name + "\',\'" + name + "\') " + camelName
    elif name.startswith("is_"):
        return "    @field(\'" + name + "\') " + camelName
    elif name.endswith("_at"):
        return "    @date(\'" + name + "\') " + camelName
    else:
        return "    @field(\'" + name + "\') " + camelName


def prepare_column_line(column):
    name = column['name']
    type = column['type']
    return get_decorator(name)


def prepare_columns(columns):
    column_string = ""
    for column in columns:
        column_string = column_string + prepare_column_line(column=column) + "\n"
    return column_string


def create_model(table):
    name = table['name']
    columns = table['columns']

    data = add_imports() + prepare_class_line(name)
    data = data + prepare_table_line(name)
    data = data + prepare_columns(columns)
    data = data + "} \n"
    data = data + prepare_export_line(name)
    return data


def create_models(f):
    json_data = get_tables_json_data(f)
    tables = json_data['tables']
    for table in tables:
        name = table['name']
        data = create_model(table)
        with open(prepare_model_name(name) + ".js", "w") as outfile:
            outfile.write(data)


if __name__ == "__main__":
    try:
        path = sys.argv[1]
        if path:
            f = open(path, "r")
            create_models(f)
        else:
            print("Provide schema.js path as first argument")
    except Exception:
        print("Provide schema.js path as first argument")
