SQL_DATA_TYPES = '''
        -- DROP TYPE "appointment_status";

        CREATE TYPE "appointment_status" AS ENUM (
        	'requested',
        	'customer_approved',
        	'master_approved',
        	'both_approved',
        	'customer_declined',
        	'master_declined');

        -- DROP TYPE "contact_type";

        CREATE TYPE "contact_type" AS ENUM (
        	'email',
        	'phone',
        	'instagram',
        	'whatsapp',
        	'telegram');

        -- DROP TYPE "membership_state";

        CREATE TYPE "membership_state" AS ENUM (
        	'inactive',
        	'active',
        	'cancel');

        -- DROP TYPE "notice_category";

        CREATE TYPE "notice_category" AS ENUM (
        	'appointment',
        	'employee');

        -- DROP TYPE "salon_type";

        CREATE TYPE "salon_type" AS ENUM (
        	'individual',
        	'chain',
        	'master');

        '''
SQL_TABLES = ''' -- addresses определение

        -- Drop table

        -- DROP TABLE addresses;

        CREATE TABLE addresses (
        	id uuid NOT NULL,
        	address text NOT NULL,
        	city text NULL,
        	country text NULL,
        	"location" geography(point, 4326) NOT NULL,
        	CONSTRAINT addresses_pkey PRIMARY KEY (id)
        );


        -- contacts определение

        -- Drop table

        -- DROP TABLE contacts;

        CREATE TABLE contacts (
        	id uuid NOT NULL,
        	created_at timestamptz NOT NULL,
        	deleted_at timestamptz NULL,
        	value text NOT NULL,
        	is_verified bool DEFAULT false NOT NULL,
        	"type" "contact_type" NOT NULL,
        	CONSTRAINT contacts_pkey PRIMARY KEY (id)
        );
        
        -- titles определение

        -- Drop table

        -- DROP TABLE titles;

        CREATE TABLE titles (
        	id uuid NOT NULL,
        	rus text NOT NULL,
         	eng text NOT NULL,
			german text NOT NULL,
			franch text NOT NULL,
        	CONSTRAINT titles_pkey PRIMARY KEY (id)
        );

        -- services определение

        -- Drop table

        -- DROP TABLE services;

        CREATE TABLE services (
        	id uuid NOT NULL,
        	created_at timestamptz NOT NULL,
        	updated_at timestamptz NULL,
        	deleted_at timestamptz NULL,
        	title text NOT NULL,
        	description text NOT NULL,
        	category text DEFAULT 'other'::text NOT NULL,
        	CONSTRAINT services_pkey PRIMARY KEY (id)
        );
        
        CREATE TABLE jsonb_services (
        	id uuid NOT NULL,
        	created_at timestamptz NOT NULL,
        	updated_at timestamptz NULL,
        	deleted_at timestamptz NULL,
        	title text NOT NULL,
        	description text NOT NULL,
        	category text DEFAULT 'other'::text NOT NULL,
			alliases jsonb NOT NULL,
        	CONSTRAINT jsonb_services_pkey PRIMARY KEY (id)
        );

        -- timetables определение

        -- Drop table

        -- DROP TABLE timetables;

        CREATE TABLE timetables (
        	id uuid NOT NULL,
        	created_at timestamptz NOT NULL,
        	deleted_at timestamptz NULL,
        	salon_id uuid NULL,
        	employee_id uuid NULL,
        	is_break bool NOT NULL,
        	day_pattern text NOT NULL,
        	time_pattern text NOT NULL,
        	CONSTRAINT checkonlyoneidisnotnull CHECK (((((salon_id IS NOT NULL))::integer + ((employee_id IS NOT NULL))::integer) = 1)),
        	CONSTRAINT timetables_pkey PRIMARY KEY (id)
        );


        -- users определение

        -- Drop table

        -- DROP TABLE users;

        CREATE TABLE users (
        	id uuid NOT NULL,
        	created_at timestamptz NOT NULL,
        	updated_at timestamptz NULL,
        	deleted_at timestamptz NULL,
        	avatar text NULL,
        	nickname text NULL,
        	contact uuid NULL,
        	"appleToken" text NULL,
        	"googleToken" text NULL,
        	CONSTRAINT "uq:users.contact" UNIQUE (contact),
        	CONSTRAINT users_pkey PRIMARY KEY (id)
        );


        -- customers определение

        -- Drop table

        -- DROP TABLE customers;

        CREATE TABLE customers (
        	id uuid NOT NULL,
        	alias text NULL,
        	contact_ids _uuid NOT NULL,
        	user_id uuid NULL,
        	CONSTRAINT customers_pkey PRIMARY KEY (id),
        	CONSTRAINT customers_user_id_fkey FOREIGN KEY (user_id) REFERENCES users(id)
        );


        -- professional определение

        -- Drop table

        -- DROP TABLE professional;

        CREATE TABLE professional (
        	id uuid NOT NULL,
        	created_at timestamptz NOT NULL,
        	deleted_at timestamptz NULL,
        	"membership_state" "membership_state" NOT NULL,
        	permission_set int8 DEFAULT '0'::bigint NOT NULL,
        	user_id uuid NOT NULL,
        	CONSTRAINT professional_pkey PRIMARY KEY (id),
        	CONSTRAINT professional_user_id_fkey FOREIGN KEY (user_id) REFERENCES users(id)
        );


        -- salons определение

        -- Drop table

        -- DROP TABLE salons;

        CREATE TABLE salons (
        	id uuid NOT NULL,
        	created_at timestamptz NOT NULL,
        	updated_at timestamptz NULL,
        	deleted_at timestamptz NULL,
        	"name" text NOT NULL,
        	"type" "salon_type" NOT NULL,
        	timezone text NOT NULL,
        	description text NULL,
        	logo text NULL,
        	active bool DEFAULT false NOT NULL,
        	address_id uuid NOT NULL,
        	timetable_id uuid NULL,
        	CONSTRAINT salons_pkey PRIMARY KEY (id),
        	CONSTRAINT salons_address_id_fkey FOREIGN KEY (address_id) REFERENCES addresses(id),
        	CONSTRAINT salons_timetable_id_fkey FOREIGN KEY (timetable_id) REFERENCES timetables(id)
        );


        -- skills определение

        -- Drop table

        -- DROP TABLE skills;

        CREATE TABLE skills (
        	id uuid NOT NULL,
        	service_id uuid NOT NULL,
        	professional_id uuid NOT NULL,
        	CONSTRAINT skills_pkey PRIMARY KEY (id),
        	CONSTRAINT skills_professional_id_fkey FOREIGN KEY (professional_id) REFERENCES professional(id),
        	CONSTRAINT skills_service_id_fkey FOREIGN KEY (service_id) REFERENCES services(id)
        );


        -- clients определение

        -- Drop table

        -- DROP TABLE clients;

        CREATE TABLE clients (
        	id uuid NOT NULL,
        	customer_id uuid NOT NULL,
        	salon_id uuid NOT NULL,
        	created_at timestamptz NOT NULL,
        	deleted_at timestamptz NULL,
        	CONSTRAINT clients_pkey PRIMARY KEY (id),
        	CONSTRAINT clients_customer_id_fkey FOREIGN KEY (customer_id) REFERENCES customers(id),
        	CONSTRAINT clients_salon_id_fkey FOREIGN KEY (salon_id) REFERENCES salons(id)
        );


        -- employees определение

        -- Drop table

        -- DROP TABLE employees;

        CREATE TABLE employees (
        	id uuid NOT NULL,
        	created_at timestamptz NOT NULL,
        	updated_at timestamptz NULL,
        	deleted_at timestamptz NULL,
        	role_set int8 NOT NULL,
        	professional_id uuid NULL,
        	salon_id uuid NOT NULL,
        	contact_ids _uuid NOT NULL,
        	CONSTRAINT employees_pkey PRIMARY KEY (id),
        	CONSTRAINT employees_professional_id_fkey FOREIGN KEY (professional_id) REFERENCES professional(id),
        	CONSTRAINT employees_salon_id_fkey FOREIGN KEY (salon_id) REFERENCES salons(id)
        );


        -- "procedures" определение

        -- Drop table

        -- DROP TABLE "procedures";

        CREATE TABLE "procedures" (
        	id uuid NOT NULL,
        	created_at timestamptz NOT NULL,
        	updated_at timestamptz NULL,
        	deleted_at timestamptz NULL,
        	duration int8 NOT NULL,
        	description text NULL,
        	price_amount numeric(10, 2) NULL,
        	price_currency text NULL,
        	service_id uuid NOT NULL,
        	employee_id uuid NOT NULL,
        	CONSTRAINT procedures_pkey PRIMARY KEY (id),
        	CONSTRAINT procedures_employee_id_fkey FOREIGN KEY (employee_id) REFERENCES employees(id),
        	CONSTRAINT procedures_service_id_fkey FOREIGN KEY (service_id) REFERENCES services(id)
        );


        -- appointments определение

        -- Drop table

        -- DROP TABLE appointments;

        CREATE TABLE appointments (
        	id uuid NOT NULL,
        	time_start timestamptz NOT NULL,
        	time_end timestamptz NOT NULL,
        	price_amount numeric(10, 2) NULL,
        	price_currency text NULL,
        	status "appointment_status" NOT NULL,
        	created_at timestamptz NOT NULL,
        	updated_at timestamptz NULL,
        	deleted_at timestamptz NULL,
        	address_id uuid NOT NULL,
        	customer_id uuid NOT NULL,
        	employee_id uuid NOT NULL,
        	CONSTRAINT appointments_pkey PRIMARY KEY (id),
        	CONSTRAINT appointments_address_id_fkey FOREIGN KEY (address_id) REFERENCES addresses(id),
        	CONSTRAINT appointments_customer_id_fkey FOREIGN KEY (customer_id) REFERENCES customers(id),
        	CONSTRAINT appointments_employee_id_fkey FOREIGN KEY (employee_id) REFERENCES employees(id)
        );
    '''
SQL_EXTANSION = '''
    CREATE EXTENSION pg_trgm
    SCHEMA public;
'''
    
SQL_DELETE_TABLES = '''
	DROP TABLE addresses CASCADE;

	DROP TABLE appointments CASCADE;

	DROP TABLE clients CASCADE;

	DROP TABLE contacts CASCADE;

	DROP TABLE customers CASCADE;

	DROP TABLE employees CASCADE;

	DROP TABLE jsonb_services CASCADE;

	DROP TABLE procedures CASCADE;

	DROP TABLE professional CASCADE;

	DROP TABLE salons CASCADE;

	DROP TABLE services CASCADE;
 	
  	DROP TABLE titles CASCADE;

	DROP TABLE skills CASCADE;

	DROP TABLE timetables CASCADE;

	DROP TABLE users CASCADE;
'''
    
    
ADDRESS = ''' 
	INSERT INTO addresses
	(id, address, city, country, "location")
	VALUES({}, {}, {}, {}, {}); 
 '''

APPOINTMENT = '''
	INSERT INTO appointments
	(id, time_start, time_end, price_amount, price_currency, status, created_at, updated_at, deleted_at, address_id, customer_id, employee_id)
	VALUES({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {});
'''

CLIENT = '''
	INSERT INTO clients
	(id, customer_id, salon_id, created_at, deleted_at)
	VALUES({}, {}, {}, {}, {});
'''
   
CONTACT = '''
	INSERT INTO contacts
	(id, created_at, deleted_at, value, is_verified, "type")
	VALUES({}, {}, {}, {}, {}, {});
'''

CUSTOMER = '''
	INSERT INTO customers
	(id, alias, contact_ids, user_id)
	VALUES({}, {}, {}, {});
'''

EMPLOYEE = '''
	INSERT INTO employees
	(id, created_at, updated_at, deleted_at, role_set, professional_id, salon_id, contact_ids)
	VALUES({}, {}, {}, {}, {}, {}, {}, {});
'''

PROCEDURE = '''
	INSERT INTO "procedures"
	(id, created_at, updated_at, deleted_at, duration, description, price_amount, price_currency, service_id, employee_id)
	VALUES({}, {}, {}, {}, {}, {}, {}, {}, {}, {});
'''

PROFESSIONAL = '''
	INSERT INTO professional
	(id, created_at, deleted_at, "membership_state", permission_set, user_id)
	VALUES({}, {}, {}, {}, {}, {});
'''

SALON = '''
	INSERT INTO salons
	(id, created_at, updated_at, deleted_at, "name", "type", timezone, description, logo, active, address_id, timetable_id)
	VALUES({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {});
'''

SERVICE = '''
	INSERT INTO services
	(id, created_at, updated_at, deleted_at, title, description, category)
	VALUES('{}', '{}', '{}', {}, '{}', '{}', '{}');
'''

SERVICE_JSON = '''
	INSERT INTO jsonb_services
	(id, created_at, updated_at, deleted_at, title, description, category, alliases)
	VALUES('{}', '{}', '{}', {}, '{}', '{}', '{}', '{}');
'''

SERVICE_TABLE = '''
	INSERT INTO titles
	(id, rus, eng, german, franch)
	VALUES('{}', '{}', '{}', '{}', '{}');
'''

SKILL = '''
	INSERT INTO skills
	(id, service_id, professional_id)
	VALUES({}, {}, {});
'''
TIMETABLE = '''
	INSERT INTO timetables
	(id, created_at, deleted_at, salon_id, employee_id, is_break, day_pattern, time_pattern)
	VALUES({}, {}, {}, {}, {}, {}, {}, {});
'''

USER = '''
	INSERT INTO users
	(id, created_at, updated_at, deleted_at, avatar, nickname, contact, "appleToken", "googleToken")
	VALUES({}, {}, {}, {}, {}, {}, {}, {}, {});    
'''

