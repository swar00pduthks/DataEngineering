# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES
# songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

songplay_table_create = ("CREATE TABLE IF NOT EXISTS songplays (songplay_id SERIAL primary key, \
                                                           start_time timestamp, user_id integer, \
                                                           level text, song_id text, artist_id text,session_id integer, location text, user_agent text, \
                           CONSTRAINT fk_userid FOREIGN KEY(user_id) REFERENCES users(user_id), \
                           CONSTRAINT fk_artistid FOREIGN KEY(artist_id) REFERENCES artists(artist_id), \
                           CONSTRAINT fk_songid FOREIGN KEY(song_id) REFERENCES songs(song_id), \
                           CONSTRAINT fk_startime FOREIGN KEY(start_time) REFERENCES time(start_time));")

user_table_create = ("CREATE TABLE IF NOT EXISTS users (user_id integer primary key, \
                                                       first_name text, last_name text, \
                                                       gender text, level text);")

artist_table_create = ("CREATE TABLE IF NOT EXISTS artists (artist_id text primary key, \
                                                       name text, location text, \
                                                       latitude decimal, longitude decimal);")

song_table_create = ("CREATE TABLE IF NOT EXISTS songs (song_id text primary key, \
                                                       title text, artist_id text, \
                                                       year integer, duration decimal, \
                    CONSTRAINT fk_sg_artistid FOREIGN KEY(artist_id) REFERENCES artists(artist_id));")

time_table_create = ("create table if not exists time ( \
                        start_time timestamp primary key, \
                        hour int, \
                        day int, \
                        week int, \
                        month int, \
                        year int, \
                        weekday int);")

# INSERT RECORDS

songplay_table_insert = ("INSERT INTO songplays (start_time,user_id,level,song_id,artist_id ,session_id ,location ,user_agent ) \
VALUES (%s, %s, %s, %s,%s,%s,%s,%s) ON CONFLICT DO NOTHING;")

user_table_insert = ("INSERT INTO users (user_id,first_name,last_name,gender,level) \
VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING;")

song_table_insert = ("INSERT INTO songs (song_id,title,artist_id,year,duration) \
VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING;")

artist_table_insert = ("INSERT INTO artists (artist_id,name,location,latitude,longitude) \
VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING; ")


time_table_insert = ("INSERT INTO time (start_time,hour,day,week,month,year,weekday) \
VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING;")

# FIND SONGS

song_select = ("select s.song_id,a.artist_id FROM songs s,artists a WHERE s.artist_id = a.artist_id \
               AND s.title = %s \
               AND s.duration = %s \
               AND a.name = %s;")

# QUERY LISTS

create_table_queries = [user_table_create, artist_table_create, song_table_create, time_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]