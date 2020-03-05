--
-- PostgreSQL database dump
--

-- Dumped from database version 12.1
-- Dumped by pg_dump version 12.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: addresses; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.addresses (
    user_id integer,
    address character varying(255),
    address2 character varying(255),
    city character varying(255),
    postal_code character varying(50),
    country_code character varying(50)
);


ALTER TABLE public.addresses OWNER TO admin;

--
-- Name: cart; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.cart (
    order_id integer,
    total_cost money
);


ALTER TABLE public.cart OWNER TO admin;

--
-- Name: countries; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.countries (
    country_code character varying(50) NOT NULL,
    name character varying(255)
);


ALTER TABLE public.countries OWNER TO admin;

--
-- Name: customers; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.customers (
    user_id integer,
    customer_money money
);


ALTER TABLE public.customers OWNER TO admin;

--
-- Name: ordered_product; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.ordered_product (
    order_id integer NOT NULL,
    user_id integer,
    product_id integer
);


ALTER TABLE public.ordered_product OWNER TO admin;

--
-- Name: ordered_product_order_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.ordered_product_order_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ordered_product_order_id_seq OWNER TO admin;

--
-- Name: ordered_product_order_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.ordered_product_order_id_seq OWNED BY public.ordered_product.order_id;


--
-- Name: products; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.products (
    user_id integer,
    product_id integer NOT NULL,
    product_name character varying(255),
    product_img text,
    product_info text,
    price numeric(13,6),
    stock integer,
    orig_price numeric(13,6),
    discount integer
);


ALTER TABLE public.products OWNER TO admin;

--
-- Name: products_product_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.products_product_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.products_product_id_seq OWNER TO admin;

--
-- Name: products_product_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.products_product_id_seq OWNED BY public.products.product_id;


--
-- Name: shops; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.shops (
    shop_id integer NOT NULL,
    user_id integer
);


ALTER TABLE public.shops OWNER TO admin;

--
-- Name: shops_shop_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.shops_shop_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.shops_shop_id_seq OWNER TO admin;

--
-- Name: shops_shop_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.shops_shop_id_seq OWNED BY public.shops.shop_id;


--
-- Name: top_selling; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.top_selling (
    product_id integer,
    buy_count integer
);


ALTER TABLE public.top_selling OWNER TO admin;

--
-- Name: users; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.users (
    user_id integer NOT NULL,
    first_name character varying(50),
    last_name character varying(50),
    birthdate date,
    gender character varying(1),
    username character varying(50),
    password character varying(50),
    email character varying(50),
    contact_no character varying(50)
);


ALTER TABLE public.users OWNER TO admin;

--
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.users_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_user_id_seq OWNER TO admin;

--
-- Name: users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.users_user_id_seq OWNED BY public.users.user_id;


--
-- Name: ordered_product order_id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.ordered_product ALTER COLUMN order_id SET DEFAULT nextval('public.ordered_product_order_id_seq'::regclass);


--
-- Name: products product_id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.products ALTER COLUMN product_id SET DEFAULT nextval('public.products_product_id_seq'::regclass);


--
-- Name: shops shop_id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.shops ALTER COLUMN shop_id SET DEFAULT nextval('public.shops_shop_id_seq'::regclass);


--
-- Name: users user_id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.users ALTER COLUMN user_id SET DEFAULT nextval('public.users_user_id_seq'::regclass);


--
-- Data for Name: addresses; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.addresses (user_id, address, address2, city, postal_code, country_code) FROM stdin;
4	Brgy. Bignay		Valenzuela City	1440	PH
\.


--
-- Data for Name: cart; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.cart (order_id, total_cost) FROM stdin;
\.


--
-- Data for Name: countries; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.countries (country_code, name) FROM stdin;
PH	Philippines
JP	Japan
UK	United Kingdom
US	Unite States of America
RU	Russia
CN	China
FR	France
\.


--
-- Data for Name: customers; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.customers (user_id, customer_money) FROM stdin;
\.


--
-- Data for Name: ordered_product; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.ordered_product (order_id, user_id, product_id) FROM stdin;
\.


--
-- Data for Name: products; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.products (user_id, product_id, product_name, product_img, product_info, price, stock, orig_price, discount) FROM stdin;
4	15	Dagat	1583442141.4029033_tokenslot_69561.jpg	Kaya mo bilhin?	5000.000000	1	1003221.000000	100
4	16	Mood Sticker	1583442209.1159222_tokenslot_WIN_20200301_00_01_15_Pro.jpg	Moody sticker	5.000000	15	100.000000	95
4	17	Red Horse	1583445278.544607_tokenslot_red_horse_1L.png	Hooooy Alak na naman!	120.000000	15	138.000000	14
\.


--
-- Data for Name: shops; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.shops (shop_id, user_id) FROM stdin;
\.


--
-- Data for Name: top_selling; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.top_selling (product_id, buy_count) FROM stdin;
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.users (user_id, first_name, last_name, birthdate, gender, username, password, email, contact_no) FROM stdin;
4	Roman	Paltera	2020-03-01	M	tokenslot	81dc9bdb52d04dc20036dbd8313ed055	rompalt37@gmail.com	92123123123
\.


--
-- Name: ordered_product_order_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.ordered_product_order_id_seq', 1, false);


--
-- Name: products_product_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.products_product_id_seq', 17, true);


--
-- Name: shops_shop_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.shops_shop_id_seq', 1, false);


--
-- Name: users_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.users_user_id_seq', 4, true);


--
-- Name: countries countries_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.countries
    ADD CONSTRAINT countries_pkey PRIMARY KEY (country_code);


--
-- Name: ordered_product ordered_product_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.ordered_product
    ADD CONSTRAINT ordered_product_pkey PRIMARY KEY (order_id);


--
-- Name: products products_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_pkey PRIMARY KEY (product_id);


--
-- Name: shops shops_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.shops
    ADD CONSTRAINT shops_pkey PRIMARY KEY (shop_id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- Name: addresses addresses_country_code_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.addresses
    ADD CONSTRAINT addresses_country_code_fkey FOREIGN KEY (country_code) REFERENCES public.countries(country_code) ON DELETE CASCADE;


--
-- Name: addresses addresses_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.addresses
    ADD CONSTRAINT addresses_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id) ON DELETE CASCADE;


--
-- Name: cart cart_order_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.cart
    ADD CONSTRAINT cart_order_id_fkey FOREIGN KEY (order_id) REFERENCES public.ordered_product(order_id) ON DELETE CASCADE;


--
-- Name: customers customers_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.customers
    ADD CONSTRAINT customers_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id) ON DELETE CASCADE;


--
-- Name: ordered_product ordered_product_product_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.ordered_product
    ADD CONSTRAINT ordered_product_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.products(product_id) ON DELETE CASCADE;


--
-- Name: ordered_product ordered_product_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.ordered_product
    ADD CONSTRAINT ordered_product_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id) ON DELETE CASCADE;


--
-- Name: products products_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id) ON DELETE CASCADE;


--
-- Name: shops shops_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.shops
    ADD CONSTRAINT shops_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id) ON DELETE CASCADE;


--
-- Name: top_selling top_selling_product_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.top_selling
    ADD CONSTRAINT top_selling_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.products(product_id) ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

