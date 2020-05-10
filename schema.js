import {appSchema, tableSchema} from '@nozbe/watermelondb'

export default appSchema({
  version: 1,
  tables: [
    tableSchema({
      name: 'users',
      columns: [
        {name: 'email', type: 'string'},
        {name: 'first_name', type: 'string'},
        {name: 'middle_name', type: 'string'},
        {name: 'last_name', type: 'string'},
        {name: 'username', type: 'string'},
        {name: 'profile_image', type: 'string'},
        {name: 'image', type: 'string'},
        {name: 'gender', type: 'string'},
        {name: 'phone_number', type: 'string'},
        {name: 'occupation', type: 'string'},
        {name: 'address', type: 'string'},
        {name: 'city', type: 'string'},
        {name: 'zip', type: 'string'},
        {name: 'state', type: 'string'},
        {name: 'country', type: 'string'},
      ],
    }),
  ],
})


