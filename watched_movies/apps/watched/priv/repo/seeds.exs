# Script for populating the database. You can run it as:
#
#     mix run priv/repo/seeds.exs
#
# Inside the script, you can read and write to any of your
# repositories directly:
#
#     Watched.Repo.insert!(%Watched.SomeSchema{})
#
# We recommend using the bang functions (`insert!`, `update!`
# and so on) as they will fail if something goes wrong.

{:ok, _movie } = Watched.Movies.create_movie(%{
    "title" => "Titanic",
    "genre" => "romance",
    "director" => "James Cameron",
    "duration" => 195,
    "release" => "1998-01-07",
    "about" => "In 1996, treasure hunter Brock Lovett and his team board the research vessel Akademik Mstislav Keldysh to search the wreck of RMS Titanic for a necklace with a rare diamond, the Heart of the Ocean. They recover a safe containing a drawing of a young woman wearing only the necklace dated April 14, 1912, the day the ship struck the iceberg. Rose Dawson Calvert, the woman in the drawing, is brought aboard Keldysh and tells Lovett of her experiences aboard Titanic."
})

{:ok, _movie } = Watched.Movies.create_movie(%{
    "title" => "The Martian",
    "genre" => "science fiction",
    "director" => "Ridley Scott",
    "duration" => 141,
    "release" => "2015-09-11",
    "about" => "In 2035, the crew of the Ares III mission to Mars is exploring Acidalia Planitia on Martian solar day (sol) 18 of their 31-sol expedition. A severe dust storm threatens to topple their Mars Ascent Vehicle (MAV). The mission is scrubbed, but as the crew evacuates, astronaut Mark Watney is struck by debris and lost in the storm. The telemetry from his suit's biomonitor is damaged and Watney is wrongly presumed dead. With the MAV on the verge of toppling, the surviving crew takes off for their orbiting vessel, the Hermes."
})

{:ok, _movie } = Watched.Movies.create_movie(%{
    "title" => "Fast & Furious 8",
    "genre" => "action",
    "director" => "F. Gary Gray",
    "duration" => 145,
    "release" => "2017-04-12",
    "about" => "Following the defeats of Deckard Shaw and Mose Jakande, Dominic Toretto and Letty Ortiz are on their honeymoon in Havana when Dom's cousin Fernando gets in trouble owing money to local racer Raldo. Sensing Raldo is a loan shark, Dom challenges Raldo to a race, pitting Fernando's reworked car against Raldo's, and wagering his own Third Generation Chevrolet Impala. After narrowly winning the race, Dom allows Raldo to keep his car, saying his respect is enough, and leaves his cousin with his own car."
})
