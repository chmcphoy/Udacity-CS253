import webapp2
from escapehtml import *
from validday import valid_day
from validmonth import valid_month
from validyear import valid_year


main_form = """
<form method="post">
    When is your birthday?
    <br>

    <label> 
        Month 
        <input type="text" name="month" value="%(month)s">
    </label>
    <label> 
        Day 
        <input type="text" name="day" value="%(day)s">
    </label>
    <label> 
        Year 
        <input type="text" name="year" value="%(year)s">
    </label>
    <div style="color: red">%(error)s</div>  
    <br>
    <br>
    <input type="submit">     
</form>
"""

class MainPage(webapp2.RequestHandler):

    def write_form(self, error="", month="", day="", year=""):
        self.response.write(main_form % {"error": error,
                                         "month": escape_html(month),
                                         "day": escape_html(day),
                                         "year": escape_html(year)})   

    def get(self):
        self.write_form() 

    def post(self):
        # below is user data
        user_month = self.request.get('month')
        user_day = self.request.get('day')
        user_year = self.request.get('year')
    
        # below is only data that's passed as valid
        month = valid_month(user_month)
        day = valid_day(user_day)
        year = valid_year(user_year)
        
        
        if not (month and day and year):
            self.write_form("That doesn't look valid to me, pal. Try Again", 
                            user_month, user_day, user_year)
        else:
            self.redirect("/thanks")
            
class ThanksHandler(webapp2.RequestHandler):

    def get(self):
        self.response.write("Thanks! That's a totally valid day!")
        
app = webapp2.WSGIApplication([('/', MainPage),
                               ('/thanks', ThanksHandler)], debug=True)
