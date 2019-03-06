from  datetime import date

MONTHS = [(1, 'Jan'), (2, 'Feb'), (3, 'Mar'), (4, 'Apr'), 
        (5, 'May'), (6, 'Jun'), (7, 'Jul'), (8, 'Aug'), (9, 'Sep'), 
        (10, 'Oct'), (11, 'Nov'), (12, 'Dec')]


COLORS = [('RGB(128, 128, 128)','RGB(128, 128, 128, 0.2)'),('RGB(255, 0, 0)','RGB(255, 0, 0, 0.2)'),
          ('RGB(0, 128, 128)','RGB(0, 128, 128, 0.2)'),('RGB(128, 0, 128)','RGB(128, 0, 128, 0.2)'),
          ('RGB(128, 0, 0)','RGB(128, 0, 0,0.2)'), ('RGB(128, 128, 0)','RGB(128, 128, 0,0.2)'),
          ('RGB(52, 152, 219)', 'RGB(52, 152, 219, 0.2)'),('RGB(33, 97, 140)','RGB(33, 97, 140, 0.2)'),  
          ('RGB(46, 204, 113)','RGB(46, 204, 113, 0.2)'),('RGB(241, 196, 15)','RGB(241, 196, 15, 0.2)'),
          ('RGB(23, 32, 42)','RGB(23, 32, 42, 0.2)'),('RGB(183, 149, 11)','RGB(183, 149, 11, 0.2)'),  
          ('RGB(0, 255, 0)','RGB(0, 255, 0, 0.2)'),('RGB(0, 255, 255)','RGB(0, 255, 255, 0.2)'),
          ('RGB(255, 0, 255)','RGB(255, 0, 255, 0.2)'),('RGB(0, 0, 255)','RGB(0, 0, 255, 0.9)')]

THIS_YEAR = date.today().year



YEARS = [str(y) for y in range(2017, THIS_YEAR + 1)]