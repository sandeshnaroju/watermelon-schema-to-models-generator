# watermelon-schema-to-models-generator
This simple python script will convert your `Watermelon`(https://github.com/Nozbe/WatermelonDB) `schema.js` tables to individual modles, like `User.js` etc.

### WHAT IS THIS ?

If you are using `Watermelon db` you, you must be familiar with `schema.js`, from which you convert to individual table models, like `User.js`, `Article.js` etc. If you have more tables, it becomes boring work to define individual Models. So, this simple python script will convert your schema to defined models. 

#### HOW TO USE?

`$ python wsm.py schema.js`

Just run the above command with `schema` file name as its first argument, that's it. It will generate your Models in the current working directory.

#### NOTE
Tested only using `Python 3.6` and `Python 3.7`
