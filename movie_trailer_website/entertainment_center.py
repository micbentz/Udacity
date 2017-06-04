"""This module contains a list of the defined movies and uses fresh_tomatoes.\
py to generate the website.
"""

import media
import fresh_tomatoes

inception = media.Movie("Inception",
                        "A thief, who steals corporate secrets through use\
                            of dream-sharing technology, is given the inverse\
                            task of planting an idea into the mind of a CEO.",
                        ("http://www.impawards.com/2010/posters/inception_ver1"
                            "2_xlg.jpg"),
                        "https://www.youtube.com/watch?v=8hP9D6kZseM")

shawshank_redemption = media.Movie("Shawshank Redemption",
                                   "Generic story line",
                                   ("https://images-na.ssl-images-amazon.com/i"
                                       "mages/I/519NBNHX5BL.jpg"),
                                   ("https://www.youtube.com/watch?v=6hB3S9bIa"
                                       "co"))

get_out = media.Movie("Get Out",
                      "Generic story line",
                      ("https://o.aolcdn.com/images/dims?resize=270%2C400&qu"
                          "ality=70&image_uri=https%3A%2F%2Fs3.amazonaws.com%2"
                          "Fmoviefone%2Fimages%2Fposters%2Fgttposter_148839768"
                          "1.jpg&client=cbc79c14efcebee57402&signature=cf4c760"
                          "5a45bdb614502afefaded2a777657f50c"),
                      "https://www.youtube.com/watch?v=sRfnevzM9kQ")

zombieland = media.Movie("Zombieland",
                         "Generic story line",
                         ("http://www.sonypictures.com/movies/zombieland/asset"
                             "s/images/onesheet.jpg"),
                         "https://www.youtube.com/watch?v=8m9EVP8X7N8")

movies = [inception, shawshank_redemption, get_out, zombieland]
fresh_tomatoes.open_movies_page(movies)
