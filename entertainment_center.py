import fresh_tomatoes
import media

#following codes are creating instances of movies. 
#to add new movie, 
#create new instance of Movie with title, description, url of image, and url of video
resident_evil6 = media.Movie('Resident Evil 6', 
                        'Long fight between human race and zombies',
                        'https://upload.wikimedia.org/wikipedia/en/thumb/a/a4/Resident_Evil_The_Final_Chapter_film_poster.jpg/220px-Resident_Evil_The_Final_Chapter_film_poster.jpg', #noqa
                        'https://www.youtube.com/watch?v=jbtmW3ydOkU')

hang_over = media.Movie('Hangover', 
                     'Field trip with full of surprises',
                     'https://upload.wikimedia.org/wikipedia/en/thumb/b/b9/Hangoverposter09.jpg/220px-Hangoverposter09.jpg', #noqa
                     'https://www.youtube.com/watch?v=tcdUhdOlz9M')

love_actually = media.Movie('Love Actually',
                            'Love stories around Chrismas',
                            'https://upload.wikimedia.org/wikipedia/en/thumb/e/eb/Love_Actually_movie.jpg/220px-Love_Actually_movie.jpg', #noqa
                            'https://www.youtube.com/watch?v=ZRUUGLkWy-s')

finding_nemo = media.Movie('Finding Nemo',
                           'Adventure of small fish',
                           'https://upload.wikimedia.org/wikipedia/en/thumb/2/29/Finding_Nemo.jpg/220px-Finding_Nemo.jpg', #noqa
                           'https://www.youtube.com/watch?v=wZdpNglLbt8')
starwars = media.Movie('Star Wars',
                        'Battle of Jedi',
                        'https://upload.wikimedia.org/wikipedia/en/thumb/3/32/Star_Wars_-_Episode_II_Attack_of_the_Clones_%28movie_poster%29.jpg/220px-Star_Wars_-_Episode_II_Attack_of_the_Clones_%28movie_poster%29.jpg', #noqa
                        'https://www.youtube.com/watch?v=gYbW1F_c9eM')
elf = media.Movie('Elf',
                  'Story about funny elf',
                  'https://upload.wikimedia.org/wikipedia/en/d/df/Elf_movie.jpg', #noqa
                  'https://www.youtube.com/watch?v=a54yC1etmVc')

#code below is creating array of movies. it will pass to fresh_tomatoes.py
#if you have added new movie, don't forget to add in to movies list
movies = [resident_evil6, hang_over, love_actually, finding_nemo, starwars, elf]

#this code called function 'open_movies_page' to display movie site
fresh_tomatoes.open_movies_page(movies)







