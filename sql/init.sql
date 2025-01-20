CREATE TABLE sbp.store_locations (
	id serial4 NOT NULL,
	city varchar(100) NOT NULL,
	"name" varchar(255) NOT NULL,
	type varchar(100) NOT NULL,
	lat FLOAT8 NOT NULL,
	lon FLOAT8 NOT NULL,
	CONSTRAINT store_locations_pkey PRIMARY KEY (id)
);

;


CREATE TABLE sbp.city_population (
	id INT4 NULL,
	city TEXT NULL,
	city_id INT4 NULL,
	area TEXT NULL,
	area_id INT4 NULL,
	office TEXT NULL,
	office_id INT4 NULL,
	group_name TEXT NULL,
	total INT4 NULL,
	age_0_5 INT4 NULL,
	age_6_18 INT4 NULL,
	age_19_45 INT4 NULL,
	age_46_55 INT4 NULL,
	age_56_64 INT4 NULL,
	age_65 FLOAT8 NULL
);

CREATE TABLE sbp.city_transportation (
stationid INT,
citycode INT,
city TEXT,
metropolincode INT,
metropolinname TEXT,
stationtypecode INT,
stationtypename TEXT,
stationoperatortypecode INT,
stationoperatortypename TEXT,
lat FLOAT,
long FLOAT)
;

CREATE TABLE sbp.bear_sheva_stores (
location_lat FLOAT,
location_lng FLOAT,
business_name TEXT,
full_address TEXT,
business_kind TEXT,
signs TEXT)
;

CREATE TABLE sbp.shopping_center (
id INT,
name TEXT,
folderpath TEXT,
description TEXT,
remarks TEXT,
shape_leng FLOAT,
shape_area FLOAT,
lat FLOAT,
lon FLOAT)
;

CREATE TABLE sbp.future_business (
id INT,
plandisgn TEXT,
landdesign TEXT,
lot TEXT,
planlot TEXT,
thickness FLOAT,
INTernet TEXT,
shape_leng FLOAT,
shape_area FLOAT,
lat FLOAT,
lon FLOAT)
;

CREATE TABLE sbp.arnona (
id INT,
city TEXT,
year INT,
price FLOAT)
;



