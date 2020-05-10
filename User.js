import {Model} from '@nozbe/watermelondb' 
import {action, field, date, relation} from '@nozbe/watermelondb/decorators' 
class User extends Model { 
 
    static table = 'users' 
 
    @field('email') email
    @field('first_name') firstName
    @field('middle_name') middleName
    @field('last_name') lastName
    @field('username') username
    @field('profile_image') profileImage
    @field('image') image
    @field('gender') gender
    @field('phone_number') phoneNumber
    @field('occupation') occupation
    @field('address') address
    @field('city') city
    @field('zip') zip
    @field('state') state
    @field('country') country
} 
export default User 
 
