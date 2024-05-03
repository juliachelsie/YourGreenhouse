# Your GreenHouse
Your GreenHouse is a blog about houseplants and indoor plants. It is also a community that hopes to gather all plant-nerds. Users can read and get tips about plants while look at beautiful images. They can also register for an account and log in, and then like and comment the blog posts. 

## Existing Features 

__Header__
- The website has a header with the text "Your GreenHouse" and a icon with a leaf. The text and the icon is in a dark green colour.

![Header](https://github.com/juliachelsie/YourGreenhouse/blob/main/media/header.PNG)

__Navbar__
- There is a navigation bar which is full responsive and includes five links to the logo, Home page, Blog posts, Contact page and to Register and sign in/log out.
It is identical on all three pages for easy navigation. On the mobile version it collapses to a menu icon. The user can easily navigate between the pages without having to revert back to previous pages via the "back"-button.

![Navbar](https://github.com/juliachelsie/YourGreenhouse/blob/main/media/navbar.PNG)

__Landing page__
- The lanfing page includes a image with a Monstera Leaf, which is suitable since it is a website about plants. There is a welcome text that explains the website and a button that takes the user directly to the blog posts. 

![Landing-page](https://github.com/juliachelsie/YourGreenhouse/blob/main/media/landingpage.PNG)

__Footer__
- The footer section includes links to social media sites for Your GreenHouse. To keep easy navigation for the user the links open in new tabs.

![Footer](https://github.com/juliachelsie/YourGreenhouse/blob/main/media/footer.PNG)

__Blog Post Site__
- The sites main functionality is the blog page. It contains all the posts with information about who wrote it, the number of likes and a image of the plant. The user can click on the post to read it.

![Blog-page](https://github.com/juliachelsie/YourGreenhouse/blob/main/media/blog.PNG)

__Blog post__
- When the user has choose a blog post and clicked it they come to a more detailed page where they can read it, they can also see comments on the post. If they are logged in they can also like and comment themself. 

![Blog-post](https://github.com/juliachelsie/YourGreenhouse/blob/main/media/blogdetails.PNG)

__Comment__
- The user can comment on blog posts. Their username, which date and time they commented will be shown. When they have clicked submit they will get a message that their comment is waiting for aproval.

![Comment](https://github.com/juliachelsie/YourGreenhouse/blob/main/media/leavecomment.PNG)
![Approval](https://github.com/juliachelsie/YourGreenhouse/blob/main/media/commentapproval.PNG)

__Contact Form__
- There is a contact form where the user can fill out a form to contact the admin of "Your GreenHouse". They will enter their name, email, the subject and a message and then click submit. The message arrives in the admin panel where the admin can read the message. 

![Contact-Form](https://github.com/juliachelsie/YourGreenhouse/blob/main/media/contactform.PNG)

__Register for a account__
- The user can register for a account to like and comment.

![Register](https://github.com/juliachelsie/YourGreenhouse/blob/main/media/signup.PNG)

__Log In__
- If the user has an account they can log in. When the user has successfully logged in they get a message with the text "Successfully signed in as (Username)"

![LogIn](https://github.com/juliachelsie/YourGreenhouse/blob/main/media/signup.PNG)

__Log Out__
- The user can of course also log out. When the user has successfully logged out they get a message with the text "You have signed out"

![Log out](https://github.com/juliachelsie/YourGreenhouse/blob/main/media/signout.PNG)

__Admin Panel__
- The website has a admin panel where the admin can handle all the blogposts. Post new blogpost, delete blog posts, approve new comments, verify email adresses, delete email adresses, read messages sent in via the contact form on the site. 

![Admin-Panel](https://github.com/juliachelsie/YourGreenhouse/blob/main/media/adminpanel.PNG)

## Design

**Colour**
- I used this color scheme on the website.
- On the header and footer there is a white background.
- On all text, except the buttons, i used #1f3a1e.
- On the text on the buttons i used #1f1e1e.
- On the background on the writer section for the blog posts I used #d6f2da.
- When the user hoovers on the ogo i used #52a84f.
- On the hearts i used #f5000.
![Colour-scheme](https://github.com/juliachelsie/YourGreenhouse/blob/main/media/palett.PNG)

**Typography**
- I used Roboto, sans serif and Lato, sans serif

## Testing

### Testing via validators

**HTML**
- I found four errors in the signup.html, but they are in the django allauth code. I don't know how to fix that without interfere with the already fixed allauth code. Otherwise there were no errors or warnings in the rest of the html code i tested in the official [W3C validator](https://validator.w3.org/nu/)

**CSS**
- No errors were returned when passing through the official [Jigsaw](https://github.com/juliachelsie/YourGreenhouse/blob/main/media/css.PNG)

**Python**
- No errors were returned when passing through the [CI Python Linter](https://pep8ci.herokuapp.com/)

**Javascript**
- No errors were returned when passing through the [JSHint](https://jshint.com/)

### Testing via lighthouse

- Index.html desktop : 
![Desktop](https://github.com/juliachelsie/YourGreenhouse/blob/main/media/index%20desktop.PNG)

- Index.html mobile : 
![Mobile](https://github.com/juliachelsie/YourGreenhouse/blob/main/media/index%20mobile.PNG)

- Post.html desktop : 
![Desktop](https://github.com/juliachelsie/YourGreenhouse/blob/main/media/post%20desktop.PNG)

- Post.html mobile : 
![Mobile](https://github.com/juliachelsie/YourGreenhouse/blob/main/media/post%20mobile.PNG)

- Details.html desktop : 
![Desktop](https://github.com/juliachelsie/YourGreenhouse/blob/main/media/comment%20desktop.PNG)

- Details.html mobile : 
![Mobile](https://github.com/juliachelsie/YourGreenhouse/blob/main/media/comment%20mobile.PNG)

- Contact.html page desktop : 
![Desktop](https://github.com/juliachelsie/YourGreenhouse/blob/main/media/contact%20desktop.PNG)

- Contact.html page mobile : 
![Mobile](https://github.com/juliachelsie/YourGreenhouse/blob/main/media/contact%20mobile.PNG)

- Signup.html desktop: 
![Desktop](https://github.com/juliachelsie/YourGreenhouse/blob/main/media/sign%20up%20desktop.PNG)

- Signup.html mobile: 
![Mobile](https://github.com/juliachelsie/YourGreenhouse/blob/main/media/sign%20up%20mobile.PNG)

- Login.html desktop : 
![Desktop](https://github.com/juliachelsie/YourGreenhouse/blob/main/media/sign%20in%20desktop.PNG)

- Login.html mobile : 
![Mobile](https://github.com/juliachelsie/YourGreenhouse/blob/main/media/sign%20in%20mobile.PNG)

- Logout.html desktop : 
![Desktop](https://github.com/juliachelsie/YourGreenhouse/blob/main/media/log%20out%20desktop.PNG)

- Logout.html mobile : 
![Mobile](https://github.com/juliachelsie/YourGreenhouse/blob/main/media/log%20out%20mobile.PNG)

### Testing with unittests in Python/Django.
- I have also used django unittest to test all my code in models.py, views.py, urls.py and forms.py. The tests are all located in tests.py. 

### Unfixed bugs
- When loading post.html lighthouse give me pretty bad "performance numbers" on both mobile and desktop devices. I think this is because the images are to big and it takes time to load. I would like to fix this issue by scaling the images down. 

### Fixed bugs
- I tried to get the links to all the pages in the navbar to softly change colour from a dark green to a light green when the user hoovers on them, but it did not work with the class names. I fixed it by putting a id on every link instead. It looks a little messy in the css but i could not find an other way to make it work. But in the end it is worth it because it looks so pretty when it changes colour. It also goes hand in hand with the logo that also changes colur when the user hovers on it. 

### How does it look on different screen sizes?

- I have tested how the website look on different screen sizes, here is the result:

- Desktop
![Desktop](https://github.com/juliachelsie/YourGreenhouse/blob/main/media/desktop.PNG)

- Tablet
![Tablet](https://github.com/juliachelsie/YourGreenhouse/blob/main/media/tablet.PNG)

- Mobile
![Mobile](https://github.com/juliachelsie/YourGreenhouse/blob/main/media/mobile.PNG)

## Deployment

### Heroku

- The steps i followed for deployment:
  I cloned the repository.
  I created a new app.
  I set the buildpacks to python and NodeJs.
  I linked the Heroku app to the repository.
  I clicked on deploy.

The live link can be found here - <>

## Credits

### Content
- I used the teaching materials from [Code Institute](https://codeinstitute.net/se/)
- The palette was created on  [Coolors](https://coolors.co/)
- The icons i used for the website was taken from [Font Awesome](https://fontawesome.com/)
- I got the favicon from [favicon.io](https://favicon.io/)
- I read about the plants and took information about them on:
[Leafy Life](https://leafy-life.com/) | 
[Southern Living](https://www.southernliving.com/) | 
[Good Housekeeping](https://www.goodhousekeeping.com/) | 
[Gardyn](https://mygardyn.com/) and
[Garderners World](https://www.gardenersworld.com/)

### Media
- All the images was taken from [FREEPIK](https://www.freepik.com/).