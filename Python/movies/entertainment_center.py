import media
import fresh_tomatoes

inception = media.Movie("Inception",
                        "Generic story line",
                        "http://a.dilcdn.com/bl/wp-content/uploads/sites/8/2013/02/toy_story_wallpaper_by_artifypics-d5gss19.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

shawshank_redemption = media.Movie("Shawshank Redemption",
                        "Generic story line",
                        "http://a.dilcdn.com/bl/wp-content/uploads/sites/8/2013/02/toy_story_wallpaper_by_artifypics-d5gss19.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

get_out = media.Movie("Get Out",
                        "Generic story line",
                        "http://a.dilcdn.com/bl/wp-content/uploads/sites/8/2013/02/toy_story_wallpaper_by_artifypics-d5gss19.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

toy_story4 = media.Movie("hello",
                        "Generic story line",
                        "http://a.dilcdn.com/bl/wp-content/uploads/sites/8/2013/02/toy_story_wallpaper_by_artifypics-d5gss19.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

toy_story5 = media.Movie("Toy Story",
                        "Generic story line",
                        "http://a.dilcdn.com/bl/wp-content/uploads/sites/8/2013/02/toy_story_wallpaper_by_artifypics-d5gss19.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

movies = [inception,shawshank_redemption,get_out,toy_story4,toy_story5]
fresh_tomatoes.open_movies_page(movies)
