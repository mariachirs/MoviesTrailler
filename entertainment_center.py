import fresh_tomatoes
import media

matrix = media.Movie("Matrix",
                            "1:30 min",
                            "Paramount",
                            "The Matrix is a 1999 science fiction \
                            film written and directed by The Wachowskis \
                            , starring Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss, Hugo Weaving, and Joe Pantoliano",
                            "https://upload.wikimedia.org/wikipedia/pt/c/c1/The_Matrix_Poster.jpg",
                            "https://www.youtube.com/watch?v=m8e-FF8MsqU")

robinhood = media.Movie("Robin Hood",
                        "1:50 min",
                        "Fox",
                        "Robin Hood is a 2010 British-American  \
                        epic war drama film based on the Robin \
                        Hood legend. ",
                        "https://upload.wikimedia.org/wikipedia/en/8/8e/Robin_Hood_2010_poster.jpg",
                        "https://www.youtube.com/watch?v=fQ6zXDSgwIY")

king_arthur = media.Movie("King Arthur",
                                 "2:20 min",
                                 "RBA",
                           "King Arthur is a 2004 epic historical fiction  \
                            war film directed by Antoine Fuqua and written  \
                            by David Franzoni",
                            "https://upload.wikimedia.org/wikipedia/en/5/59/Movie_poster_king_arthur.jpg",
                            "https://www.youtube.com/watch?v=fqZh1tg_bF4")

friends = media.Serie("Friends",
                            "33 min",
                                 "BCS",
                           "Friends is an American television sitcom \
                            a group of frieds decide live together \
                            funny moments will happen",
                            "http://images6.fanpop.com/image/forum/topics/0/863_1352903304807_full.jpg",
                            "https://www.youtube.com/watch?v=hDNNmeeJs1Q",
                            "236 episodes")

walkingdead = media.Serie("The Walking Dead",
                            "45 min",
                                 "AMC",
                           "The chaos, zombies and a lot of gore \
                            Is possible survice in this situation, \
                            Sheriff Rick will struglle to keep his family alive",
                            "https://http2.mlstatic.com/S_575201-MLB8487493651_052015-O.jpg",
                            "https://www.youtube.com/watch?v=R1v0uFms68U",
                            "60 episodes")


series = [friends, walkingdead]

movies = [matrix, robinhood, king_arthur]

#Send movies and series to showed into client side
fresh_tomatoes.open_movies_page(movies, series)
