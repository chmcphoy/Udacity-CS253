months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']

months_abbr = dict((m[:3].lower(), m) for m in months)

          
def valid_month(month):
    if month:
        foo = month[:3].lower()
        return months_abbr.get(foo)
