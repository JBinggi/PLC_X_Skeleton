# oneplace-skeleton

Building a module in onePlace can be really simple, once you learn a couple of quirks. 
The goal of this post is to create a skeleton plugin and introduce you to the basics.

The skeleton module gives you a starting point for creating any Webbased, data driven
App you can imagine. Want to manage your Contacts, Articles, Books, Albums, Worktimes,
Members, whatever you can imagine. 

onePlace gives you the tools to just develop a webapp on the fly based on a database model.
onePlace will create all the views / Html for you.

## The form generator
![Form Generator](https://docs.1plc.ch/img/formgenerator.png)

OnePlace will create all forms for you on the fly. Just choose the fields you want to have
for your module and onePlace will deploy them. We have designed onePlace to be able to handle
large forms with dozens, even hundreds of fields but still have a usable and clean interface.

So you will be able the model even the most complex data within onePlace.

So for example you want to manage Books. Skeleton will give you Books with "Titles"
by default. Now you can extend those Books by "Date received", "Deadline return", "Current Owner",
and so on - all just by the click of a button ! Not a single line of Code is needed.

## How to add new fields

All you have to do is to run the install sql snippet from your 
[dynamic fields docs](https://docs.1plc.ch/oneplace-skeleton/dynamic-fields/) to add your extra field to your skeleton
module. 

Here is a small example of how to add a new textfield to skeleton

```sql
ALTER TABLE `skeleton` ADD `lastname` TEXT NOT NULL DEFAULT '' AFTER `label`; 

INSERT INTO `core_form_field` (`Field_ID`, `type`, `label`, `fieldkey`, `tab`, `form`, `class`, `url_view`, `url_ist`, `show_widget_left`, `allow_clear`, `readonly`, `tbl_cached_name`, `tbl_class`, `tbl_permission`) VALUES 
(NULL, 'text', 'Lastname', 'lastname', 'skeleton-base', 'skeleton-single', 'col-md-3', '', '', '0', '1', '0', '', '', ''); 
```

And done ! Your skeleton now has a new textfield "Lastname", which can be shown in add form, edit form.
view template, and index for skeletons as index row selectable for users ! also its added to the list
API of your skeleton. And this way you can add as many fields of whatever type you like.

We have some more advanced examples in the [Examples Section](https://docs.1plc.ch) 

Also we are working towards a full GUI For this process - so you will be able to just add
new fields on the fly within the onePlace Admin Interface.

## Dynamic Index Pages
![Form Generator](https://docs.1plc.ch/img/indexpages.png)

onePlace will create Dynamic Index Pages for your Skeleton Module. Based on your dynamic
form fields, you will be able to set the allowed index columns for each user. the users
can then sort the index columns by drag & drop for themself.

You also have paging to handle large datasets enabled by default. 10,25,50,100,250 are
the default options. the settings are user based.

As with every other dynamic page, you also have the dynamic button panel where you can
show custom buttons for every action you like, optionally filtered based on permissions.

## Enhance Skeleton with own code

The best of it all - if you like to enhance it, just fork the skeleton module and implement
your changes. We gave our best to find a design that allows you to make your customizations
but still be update compatible with the main skeleton module.

There is already over 60 modules based on Skeleton like Contacts, Articles, Onlineshops, Events,
Members and many more. 

You can use all the skeleton compatible plugins for your own module like tags, (categories,states,many more)
Gamification (User Leveling & Achievements), strong whitelist routing for fort knox like security and much more.

Just focus on your business logic and let onePlace do the rest for you.

Learn more about how to code your own onePlace module with the [Album Tutorial](https://docs.1plc.ch) 

## Support
 * Issues: [github.com/oneplc/plc_x_skeleton/issues](https://github.com/oneplc/plc_x_skeleton/issues)
 * Source: [github.com/oneplc/plc_x_skeleton/](https://github.com/oneplc/plc_x_skeleton/)
 * Telegram Group: [t.me/oneplc](https://t.me/oneplc)