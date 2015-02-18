ABOUT
-----
An alternative to Django flatpages without the sites requirement, but with 
some newer features.

QUICK START
-----------

SETTINGS
--------

**Page Templates** Default::

    PAGE_TEMPLATES = (
        ('pages/default.html', 'Default'),
    )

A list of two-tuples in the format (``filename``, ``template name``). 

You can add more template choices by extending this list::

    PAGE_TEMPLATES = (
        ('pages/default.html', 'Default'),
        ('pages/two-column.html', 'Two Column'),
    )

LICENSE
-------
Copyright (C) 2014

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

CREDITS
-------
A project by [Water.org](http://water.org/). For more than two decades,
Water.org has been at the forefront of developing and delivering solutions to
the water crisis. Founded by Gary White and Matt Damon, Water.org pioneers
innovative, community-driven and market-based solutions to ensure all people
have access to safe water and sanitation; giving women hope, children health
and communities a future. To date, Water.org has positively transformed the
lives of more than 1,000,000 individuals living across communities in Africa,
South Asia, Latin America and the Caribbean; ensuring a better life for
generations ahead.
