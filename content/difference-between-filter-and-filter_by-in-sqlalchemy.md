Title: SQLAlchemy中filter和filter_by的区别
Date: 2014-06-19 20:35
Category: Python
Tags: Flask
Slug: difference-between-filter-and-filter_by-in-sqlalchemy

* filter_by用于简单的列名查询，如：

  `db.users.filter_by(name='Joe')`
  
* filter对于上面的代码可以这样写：

  `db.users.filter(db.users.name=='Joe')`
  
* 对于复杂的查询使用filter，如：

  `db.users.filter(or_(db.users.name=='Ryan', db.users.country=='England'))`
  
**注意：filter使用的是赋值=，而filter使用的是判断==**

*另外：查询时使用like这样写：*
  `items = Item.query.filter(Item.user == current_user, Item.title.like('%' + keyword + '%')).all()`
  
参考：[http://stackoverflow.com/questions/2128505/whats-the-difference-between-filter-and-filter-by-in-sqlalchemy](http://stackoverflow.com/questions/2128505/whats-the-difference-between-filter-and-filter-by-in-sqlalchemy)