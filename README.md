# The Lost Tapes

The Lost Tapes is a website dedicated to music album reviews. The Lost Tapes gives user to read album reviews, write their own album reviews, edit and delete their reviews. Users can also interact with each other in the comment section allowing a community driven ethos which permiates throughout the site. The lost tapes is virtual world where music lovers can share their takes on the latest, or classic, albums and discuss their views and opiniosn on released albums. 

## UX 

The purpose of this website is to deliver a blog-style music site which allows users to create, read, update, and delete reviews. The target auidence for this site is people who are interested in music and would like to read and share the opinions of others on album releases. 


### Project Goals 

The main goal of this website was to deliver CRUD functionality to a blog-style review site. Users can create, read update and delete their own reviews. As well as creating their own reviews they can comment on other's psots and 'like' the posts. 

### User Goals 

### User
As a site user I can register account so that I can interact with site content.

As a site user I can view a paginated list of posts so that I can easily select a post to view.

As a site user I can view a list of reviews so that I can select one to read.

As a site user I can click on a review so that I can read a full review.

As a site user I can create, read update and delete posts so that I can manage my blog content.

As a site user I can like or unlike a post so that I can interact with the content.

As a site user I can create drafts so that I can finish writing site content later.

As a user I can comment on a post so that I can be involved in the post discussion.

As a user I can add comments to a post so that I can be involved in discussion.


As a user I can search the website for a post so that I can quickly find whether the site has the post I am looking for.


### Admin 
As a site admin I can approve or disapprove user uploaded content so that I can manage site content.


## User Expectations 
As there is a specific target audience, music enthusiasts, for this website the following user expectations were considered when creating the site:

* The site is simple, clear and easy to use.
* The structure is logical and obvious.
* The site is responsive and users can expect to see the same content on different devices without a reduction in quality.
* The media content is relevant to the albums listed
* There ability for users to easily navagate the website and search for a specific review. 
* Users can cleary read and interact with the website and the reviews. 

## User Stories 

User stories were utilised throughout to manage features. Features were implemented based on the to do - in progress - done structure. 


User stories were produced to guide each feature stage of the site.
![user stories to do ](documentation_assets/images/inital_user_story.webp)


Whilst a feature was being worked on, it was moved to the 'in progress' section
![user stories in progress](documentation_assets/images/inprogressus.webp)


Once a feature was completed, it was moved over to the done section 
![user stories in progress](documentation_assets/images/doneus.webp)


## Strategy 

In order to create a site which is relevant to its target auidence, various other related website were researched first in order to comprehensively analyse the features which would be necessary. 

| Feature        | Importance   | Viability |
| ------------- |:-------------:| -----:|
| Display a list of album reivews     | 5 | 5  |
| open a specific album review      | 5      |   5 |
| User sign up | 5      |    5 |
| User CRUD functionality | 5      |    5 |
| User can draft posts | 4      |    5 |
| paginate list of reviews | 5      |    5 |
| Responsive design | 5      |    5 |
| User comments | 4      |    4 |
| User likes / unlikes | 3      |    4 |
| Admin approval of comments | 4      |    5 |
| Users can search for content | 3      |    4 |
| Users have a page of their own content | 2      |    3 |


## Structure 

### Database Model

Planned database model 

![database model sketch](documentation_assets/images/databasemodelsketch.webp)


Final database model 

![final dataebase model](documentation_assets/images/finaldatabase.webp)

![final dataebase model2](documentation_assets/images/finaldatabasesecond.webp)


## Design 

### Wireframes 

Before building the site, Balsamiq was utilised to create wireframes of the site. Wireframes were created in order to develop the websites asthetic and to give an impression of the responsive style across different platforms. 

#### Desktop Homepage 
![desktop Homepage](documentation_assets/wireframes/homepage_desktop.webp)

#### Desktop All Reviews Page
![desktop Review Page](documentation_assets/wireframes/reviewpage_desktop.webp)

#### Desktop Album Reviews Page
![album review page](documentation_assets/wireframes/album_review.webp)

#### Desktop Add Review Page
![desktop add review page](documentation_assets/wireframes/add_review.webp)

#### Desktop Edit review Page
![desktop edit review page](documentation_assets/wireframes/edit_review.webp)

#### Desktop Delete Review 
![desktop delete review](documentation_assets/wireframes/delete_review.webp)

#### Desktop Sign In  
![desktop sign in page](documentation_assets/wireframes/sign_in.webp)

#### Desktop Sign Up
![desktop sign up](documentation_assets/wireframes/sign_up.webp)

#### Desktop Sign Out
![desktop sign out](documentation_assets/wireframes/sign_out.webp)

#### Mobile Home Page
![mobile home page](documentation_assets/wireframes/mob_home.webp)

#### Mobile All Review Page
![mobile review page](documentation_assets/wireframes/mob_review.png)

#### Mobile Review Detail Page
![mobile review detail page](documentation_assets/wireframes/mob_review_details.webp)

#### Mobile Add Review 
![mobile add reivew](documentation_assets/wireframes/mob_add_review.webp)

#### Mobile Edit Review
![mobile edit review](documentation_assets/wireframes/mob_edit_review.webp)

#### Mobile Delete Review
![mobile delete review](documentation_assets/wireframes/mob_delete.webp)

#### Mobile Sign In 
![mobile sign in review](documentation_assets/wireframes/mob_sign_in.webp)
#### Mobile Sign Up
![Mobile Sign Up](documentation_assets/wireframes/sign_up.webp)

#### Mobile Sign Out
![Mobile Sign Out](documentation_assets/wireframes/mob_signout.webp)



### Colour Schemes

During the inital design phase, I researched a variety of music review based websites. A common theme across the websites is their commitment to netrual and simplified colour schemes. I adapted this approach when designing my site. The reasoning for this choice is that when users upload album artwork, it can  be in a variety of different colours and styles which could potentially clash with an over exhuberant colour scheme design choice. Keeping a sleek, schematic colour scheme minimises any potential clashes with user uploaded image content and keeps the site asthetically pleasing for the user. White, black and sublte grey on the footer and header were used to keep the colour schemes formularized. 

### Fonts

Andada Pro was chosen at the primary font choice throughout the website. After experimenting with a variety of fonts, Andada Pro provided sleek serif typography which complimented the overall professional, yet calm asthetic of the website. San-serif was chosen as a backup font, should Andada Pro fail. 


# Features 

### Nav Bar 

Every page of the site contain a navigation bar with links to different pages of the site. Each of the links highlight when hovered over to indicate what the user is about to click on. The page which the user is on is highlighed on the navigation bar. The navagation links differ depending if the user is logged in and authenticated or not logged in. 

When logged out the nav bar displays a 'log in' and 'register' link. 
![logged out navbar](documentation_assets/images/nav_bar_logged_out.png)


When the user is logged in the nav bar displays the links 'write a post' 'your posts' and 'log out'

![logged in navbar](documentation_assets/images/loggedin_in_nav.png)


Users can use the seach bar to search the site for a specific album review. 
![search bar](documentation_assets/images/search.png)


### Footer

The footer features on each page. Footer icon links enlarge when hovered over and links open in a seperate page as to note pull the user away from the site.
![footer](documentation_assets/images/footer .png)

### Homepage 

The home page features a hero image with a short overview of what the sebsite is about. 
![Hero Image](documentation_assets/images/heroimage.png)


The home page features the latest 4 reviews uploads. 
![Home Page Reviews](documentation_assets/images/homepage_lr.png)

### Account pages

When a user clicks on the log in page they are asked to sign in with their username and password

![sign in](documentation_assets/images/signin.png)

When a user selects the register they are presented with a registrated form with an option email form detail. 

![Register](documentation_assets/images/register.png)

Whilst signed in, users can logg out by clicking on the sign out link which will ask users to confirm signing out 
![Signout](documentation_assets/images/signout.png)


### Add Review Page

When user is logged in they can add their own review. They are presented with a form where they can input: Album title, artist, genre, an album image, their score out of 10 and their review. Users also have the option to publish straight away or to draft the post and return to it later. The slug for the post is automatically generated so the user does not have the option to decide their own slug. 

![review page](documentation_assets/images/add_review_one.webp)

For the review body, crispy forms was added so users can have some autonomy on the presentation of their review. Some aspects of cirspy forms were removed from the user however, such as the ability to add images into the body in order to keep the form congruent. 
![review page](documentation_assets/images/add_review_two.webp)

### Your posts 

Once signed in, users have the ability to navagate to a page which holds all of their reviews on. From here users, can see all of their posts; published or unpublished.
![Your posts page](documentation_assets/images/your_posts.webp)

Users can manage their posts here by edit and delete buttons.
 
![edit and delete buttons](documentation_assets/images/edit_delete.webp)


### Edit & Delete Posts

Users can edit their posts either published or unpublished. 
![Edit Post](documentation_assets/images/your_posts.webp)


If a user clicks on 'delete posts' they will be asked again to ensure they want to delete the posts where a larger delete button will appear. Once they click delete again the post will be deleted. 
![Delete Post](documentation_assets/images/delete_post.webp)

### Search Posts

Users can ultilise the search bar to search the site for reviews. If the searched word appears in the album title or the artist name, the post will be displayed. 
![Search Post](documentation_assets/images/search_posts.webp)

### Messaging 

When users perform certain actions on the site, they will be informed via messaging so it is explicity stated what action they have just performed. 

Creating a new post 
![creating a new post](documentation_assets/images/create_message.png)

Updating a post 
![updating new post](documentation_assets/images/update_message.png)

Deleting a post 

![deleting a post](documentation_assets/images/delete_message.png)


signing in 
![signing in](documentation_assets/images/sign_in_message.png)

# Testing

### Google developer tools
Google chrome developer tools were utilised throughout the building of this website. Elements on the page were maniuplated through the google developer tools and then implemented permanently 

### Manual Testing
Different browsers were used to test the site to ensure cross compatibility including :

* Safari
* Firefox
* Googlechrome


Manual testing on devices was also undertaken, devices tested include:

* Iphone X
* Ipone 11
* Ipad
* Huawei p30

## Feature Testing 

### Navagation  

| Feature        | Test    | Outcome |
| ------------- |-------------| -----|
| Logo   | Does the logo linkback to homepage | PASS  |
| Home Button | Does the home link direct users to home page? Does the hover effect work when mouse hovers over button? Is the button highlighted with the page is active?  | PASS |
| Reviews Button | Does the reviews link direct users to reviews page? Does the hover effect work when mouse hovers over button? Is the button highlighted with the page is active?    |    PASS |
| Log In Button | Does the Log in link direct users to Log In page? Does the Log In link only appear when users are logged out ? Does the hover effect work when mouse hovers over button? Is the button highlighted with the page is active?  |    PASS|
| Register | Does the Register link direct users to Register page? Does the Register link only appear when users are logged out ? Does the hover effect work when mouse hovers over button? Is the button highlighted with the page is active?      |    PASS |
| Search Bar | Can user use key words to search for a post?      |    PASS |


### Footer 
| Feature        | Test    | Outcome |
| ------------- |-------------| -----|
| Facebook   | Does the icon increase in size when hovered over? Does the icon open in a new browser page when clicked on ? | PASS  |
| Twitter | Does the icon increase in size when hovered over? Does the icon open in a new browser page when clicked on ?  | PASS |
| YouTube | Does the icon increase in size when hovered over? Does the icon open in a new browser page when clicked on ?  | PASS |
| Instagram | Does the icon increase in size when hovered over? Does the icon open in a new browser page when clicked on ?  | PASS |


### Home page
| Feature        | Test    | Outcome |
| ------------- |-------------| -----|
| Hero Image   | Is the hero image responsive on multiple devices? | PASS  |
| Album reviews | Are they a maximum of 4 album reviews displayed which are responsive to different devices  | PASS |
| Heading & Paragraphs | Are the headings and paragraphs responsive on multiple devices? Do the headings maintain congruence?  | PASS |

### Review Page 
| Feature        | Test    | Outcome |
| ------------- |-------------| -----|
| Album reviews | Are they a maximum of 8 album reviews displayed which paginated onto a new page once reached the maximum and are responsive to different devices   | PASS |
| Heading | Are the headings responsive on multiple devices? Do the headings maintain congruence?  | PASS |

### Sign In Page 

| Feature        | Test    | Outcome |
| ------------- |-------------| -----|
| Sign up form | Can users sign in using their registered details? Is the form responsive on multiple devices ?   | PASS |
| Heading | Are the headings responsive on multiple devices? Do the headings maintain congruence?  | PASS |

### Sign Up Page 

| Feature        | Test    | Outcome |
| ------------- |-------------| -----|
| Sign up form | Can users register to sign up with a user name and the option of adding an email address? Is the form responsive on multiple devices ?   | PASS |
| Heading | Are the headings responsive on multiple devices? Do the headings maintain congruence?  | PASS |


### Sign Out Page 
| Feature        | Test    | Outcome |
| ------------- |-------------| -----|
| Sign Out |Can users sign out ? Are users redirected to the home page once signed out?   | PASS |
| Heading | Are the headings responsive on multiple devices? Do the headings maintain congruence?  | PASS |


### Write a review page  
| Feature        | Test    | Outcome |
| ------------- |-------------| -----|
| Review Form | Can users add their own album title, artist, genre, image, and text ? | Pass |
| Summernote body | Is summernote utilised for the body of the review?  | PASS |
| Publish / draft | Can a user decide to draft or publish their post ? | PASS |
| Slug | Is a slug automatically generated? | PASS |
| Heading | Are the headings responsive on multiple devices? Do the headings maintain congruence?  | PASS |

### Edit a review page  
| Feature        | Test    | Outcome |
| ------------- |-------------| -----|
| Review Form | Can users edit their own album title, artist, genre, image, and text ? Is the previous data inputted from the user still visible? | Pass |
| Summernote body | Is summernote utilised for the body of the review?  | PASS |
| Publish / draft | Can a user decide to draft or publish their post ? | PASS |
| Heading | Are the headings responsive on multiple devices? Do the headings maintain congruence?  | PASS |

### Delete a review  
| Feature        | Test    | Outcome |
| ------------- |-------------| -----|
| Review Form | Can users delete their reivew? | Pass |
| Warning | Are users asked a second time whether they want to delete their post ?  | PASS |
| Heading | Are the headings responsive on multiple devices? Do the headings maintain congruence?  | PASS |

### Search Page
| Feature        | Test    | Outcome |
| ------------- |-------------| -----|
| Search Bar | Can users, use key words to search for a review ? | Pass |
| Search results | Are results which include the users searched words in the title or artist displayed ?  | PASS |
| case sensitivity | Are the search results non-case-sensitive so the results display irrespective of uppercase or lowercase ?  | PASS |
| Heading | Are the headings responsive on multiple devices? Do the headings maintain congruence?  | PASS |


# Validation 

W3C Validator was used to check for error within my HTML code.

The final check presented error free HTML

Index Page
![index page validation](documentation_assets/images/index_validation.png)

Review Page
![Review Page Validation](documentation_assets/images/main_review_page.png)

Search Page
![Search Page Validation](documentation_assets/images/searchpage.png)

Your Posts
![Your Posts validation](documentation_assets/images/yourposts.png)

Sign In Page
![Sign In validation](documentation_assets/images/signinpage.png)

Sign Out Page
![sing out validation](documentation_assets/images/signout_page.png)

Sign Up Page
![Sign Up validation](documentation_assets/images/signuppage.png)
* Come back to this section 


### CSS
The CSS passed through the validator without any issues.

![Main review page](documentation_assets/images/cssvalidator.png)

### Python validation

PEP8 Validator was used to check for errors within the python files. The finalised Python files were error free. 

admin.py Validation
![admin.py Validation](documentation_assets/images/adminpyvalidation.png)

apps.py Validation
![apps.py Validation](documentation_assets/images/appsvalidation.png)

asgi.py Validation
![asgi.py Validation](documentation_assets/images/asgivalidation.png)

forms.py Validation
![forms.py Validation](documentation_assets/images/formspyvalidation.png)

urls.py Validation
![mainurls.py Validation](documentation_assets/images/mainurlsvalidation.png)

models.py Validation
![models.py Validation](documentation_assets/images/modelspyvalidation.png)

app urls.py Validation
![urls.py Validation](documentation_assets/images/urlspyvalidation.png)


view.py Validation
![view.py Validation](documentation_assets/images/viewspyvalidation.png)

wisgi.py Validation
![wisgi.py Validation](documentation_assets/images/wisgi_validation.png)


## Lighthouse validation

Lighthouse was utilised to test the performance, accessibility, best practices and SEO of the website. Both desktop and mobile were tested. On mobile testing, pages with summernote the performance was downgraded. 

Home page validation desktop 
![Home page validation desktop](documentation_assets/lighthouse/homepage_desktop.png)


Home page validation mobile 

![Home page validation mobile](documentation_assets/lighthouse/homepage_mob.png)

Review page validation desktop
![Review page validation desktop](documentation_assets/lighthouse/reviewspage_desktop.png)

Review page validation mobile
![Review page validation mobile](documentation_assets/lighthouse/register_mob.png)

Your Posts validation desktop
![Your Posts validation desktop](documentation_assets/lighthouse/yourposts_desktop.png)

Your Posts validation mobile
![Your Posts validation mobile](documentation_assets/lighthouse/yourposts_mob.png)

Main Review Page Desktop
![Your Posts validation mobile](documentation_assets/lighthouse/mainreview_desktop.png)


Main Review Page Mobile 
![Your Posts validation mobile](documentation_assets/lighthouse/mainrevew_mob.png)

Search Page Desktop
![Search Page Desktop](documentation_assets/lighthouse/searchpage_desktop.png)

Search Page Mobile
![Search Page Mobile](documentation_assets/lighthouse/search_mob.png)

Write Review desktop
![Write Review desktop](documentation_assets/lighthouse/writereview_desktop.png)

Write Review mobile
![Write Review mobile](documentation_assets/lighthouse/write_review_mob.png)

Edit Review desktop
![Edit Review desktop](documentation_assets/lighthouse/edit_review_desktop.png)

Edit Review mobile 
![Edit Review mobile](documentation_assets/lighthouse/edit_review_mob.png)

Delete Review Desktop
![Delete Review Desktop](documentation_assets/lighthouse/delete_page_desktop.png)

Delete Review Mobile
![Delete Review Mobile](documentation_assets/lighthouse/delete_page_mob.png)

Sign in Desktop
![sign in Desktop](documentation_assets/lighthouse/signin_desktop.png)

Sign in Mobile
![sign in Mobile](documentation_assets/lighthouse/sign_in_mob.png)

Sign out Desktop
![sign out desktop](documentation_assets/lighthouse/signout_desktop.png)

Sign out mobile
![sign out mobile](documentation_assets/lighthouse/signout_desktop.png)

Register Page Desktop
![Register Page Desktop](documentation_assets/lighthouse/register_desktop.png)

Register Page Mobile
![Register Page Mobile](documentation_assets/lighthouse/register_mob.png)

# Bugs 

## Solved bugs

* Initally, the 'edit' page did not allow me to update the image field from the already previously set image. This bug was solved by adding a 'enctype="multipart/form-data' to the form which solved the bug. 

* When connecting URLS my 'create post' page would not route to the page. Instead a 404 error message would be displayed. This was solved by rearraging the order of the URLS. 

The 'create post' url was put above the 'slug' url to solve this issue. 
![url bug](documentation_assets/images/url_bug.webp) 

* When connecting summernote to the 'body' of the create/edit album review, the sizing did not match rest of the formatting of the page. When reading the documentation I discovered this bug was solved by adapting the summernote configuration in the settings. 
![summernote bug](documentation_assets/images/summer_note.webp)


* When bulding the comment section on my site, I recieved an IntegrityError when trying to post a comment. This bug was caused by a missing line of code in the views.py file

This bug was solved by adding this line into the views file. 
![comment bug](documentation_assets/images/comment_bug.webp)