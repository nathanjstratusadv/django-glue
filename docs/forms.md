## Form Structure 
- Django Glue fields work with model objects. 
- They pull the necessary context data from the model field to build the html attributes needed to render the form fields.
- The form fields on the front end, configure themselves to glue object in alpine js.
- Glue Model Object handler returns Glue Model Object Fields. 
- Each Glue Model Field has name, type, value and html attrs. 
- Html attrs are generated from our form module. It needs a model field, to find the type and build the Attrs.
- It indexes the glue field attr factory map to find the type of the model. 
- Glue Attr factory has a factory method that returns the glue html attrs.
- Do I need the factories and the html attrs separated? 
  - Factories parse the information from the model and initialize the attrs
  - Glue Field attrs has the logic to manipulate the data to turn it into the actual code needed for the front end. 
  - Just have a factory that return a dict of html attrs?