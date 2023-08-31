def modified_movies(etl_state: str) -> str:
    return f"""
select
	fw.id,
	fw.rating,
	fw.title,
	fw.description,
	fw.creation_date,
    fw.image_url,
	json_agg(distinct jsonb_build_object('id', p.id, 'name', p.full_name)) persons,
	json_agg(distinct jsonb_build_object('id', g.id, 'name', g.name)) genres,
	max(greatest(fw.modified, p.modified, g.modified)) modified
	
from content.film_work fw
left join content.person_film_work pfw on fw.id = pfw.film_work_id
left join content.genre_film_work gfw on fw.id = gfw.film_work_id
left join content.person p on p.id = pfw.person_id
left join content.genre g on g.id = gfw.genre_id 
where fw.modified > '{etl_state}' or p.modified > '{etl_state}' or g.modified > '{etl_state}'
group by
	fw.id,
	fw.rating,
	fw.title,
	fw.description,
	fw.creation_date;
"""


def modified_genres(etl_state: str) -> str:
    return f"""
select 
	g.id,
	g.name,
	g.description,
	array_agg(fw.id) films,
	avg(fw.rating) rating,
    max(greatest(g.modified, fw.modified)) modified
from content.genre g
left join content.genre_film_work gfw on g.id = gfw.genre_id
left join content.film_work fw on gfw.film_work_id = fw.id
where g.modified > '{etl_state}' or fw.modified > '{etl_state}'
group by
	g.id,
	g.name,
	g.description;
"""


def modified_persons(etl_state: str) -> str:
    return f"""
select
	p.id,
	p.full_name,
    p.image_url,
	avg(fw.rating) rating,
	array_agg(fw.id) films,
    max(greatest(p.modified, fw.modified)) modified
	
from content.person p
left join content.person_film_work pfw on p.id = pfw.person_id
left join content.film_work fw on pfw.film_work_id = fw.id
where p.modified > '{etl_state}' or fw.modified > '{etl_state}'
group by
	p.id,
	p.full_name;
"""
