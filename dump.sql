--
-- PostgreSQL database dump
--

-- Dumped from database version 12.8 (Ubuntu 12.8-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 12.8 (Ubuntu 12.8-0ubuntu0.20.04.1)

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
-- Name: auteurs; Type: TABLE; Schema: public; Owner: ubikadmin
--

CREATE TABLE public.auteurs (
    id integer NOT NULL,
    nom character varying(20),
    prenom character varying(20)
);


ALTER TABLE public.auteurs OWNER TO ubikadmin;

--
-- Name: auteurs_id_seq; Type: SEQUENCE; Schema: public; Owner: ubikadmin
--

CREATE SEQUENCE public.auteurs_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auteurs_id_seq OWNER TO ubikadmin;

--
-- Name: auteurs_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ubikadmin
--

ALTER SEQUENCE public.auteurs_id_seq OWNED BY public.auteurs.id;


--
-- Name: livres; Type: TABLE; Schema: public; Owner: ubikadmin
--

CREATE TABLE public.livres (
    id integer NOT NULL,
    titre character varying(20),
    date timestamp without time zone,
    auteur_id integer NOT NULL
);


ALTER TABLE public.livres OWNER TO ubikadmin;

--
-- Name: livres_id_seq; Type: SEQUENCE; Schema: public; Owner: ubikadmin
--

CREATE SEQUENCE public.livres_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.livres_id_seq OWNER TO ubikadmin;

--
-- Name: livres_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ubikadmin
--

ALTER SEQUENCE public.livres_id_seq OWNED BY public.livres.id;


--
-- Name: tag_livre; Type: TABLE; Schema: public; Owner: ubikadmin
--

CREATE TABLE public.tag_livre (
    tag_id integer NOT NULL,
    livre_id integer NOT NULL
);


ALTER TABLE public.tag_livre OWNER TO ubikadmin;

--
-- Name: tags; Type: TABLE; Schema: public; Owner: ubikadmin
--

CREATE TABLE public.tags (
    id integer NOT NULL,
    titre character varying(20)
);


ALTER TABLE public.tags OWNER TO ubikadmin;

--
-- Name: tags_id_seq; Type: SEQUENCE; Schema: public; Owner: ubikadmin
--

CREATE SEQUENCE public.tags_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tags_id_seq OWNER TO ubikadmin;

--
-- Name: tags_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ubikadmin
--

ALTER SEQUENCE public.tags_id_seq OWNED BY public.tags.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: ubikadmin
--

CREATE TABLE public.users (
    id integer NOT NULL,
    nom character varying(20),
    prenom character varying(20),
    login character varying(10),
    password character varying(10)
);


ALTER TABLE public.users OWNER TO ubikadmin;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: ubikadmin
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO ubikadmin;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ubikadmin
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: auteurs id; Type: DEFAULT; Schema: public; Owner: ubikadmin
--

ALTER TABLE ONLY public.auteurs ALTER COLUMN id SET DEFAULT nextval('public.auteurs_id_seq'::regclass);


--
-- Name: livres id; Type: DEFAULT; Schema: public; Owner: ubikadmin
--

ALTER TABLE ONLY public.livres ALTER COLUMN id SET DEFAULT nextval('public.livres_id_seq'::regclass);


--
-- Name: tags id; Type: DEFAULT; Schema: public; Owner: ubikadmin
--

ALTER TABLE ONLY public.tags ALTER COLUMN id SET DEFAULT nextval('public.tags_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: ubikadmin
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: auteurs; Type: TABLE DATA; Schema: public; Owner: ubikadmin
--

COPY public.auteurs (id, nom, prenom) FROM stdin;
1	Manu	Zak
3	Erik	Zak
2	Miko	Zak
\.


--
-- Data for Name: livres; Type: TABLE DATA; Schema: public; Owner: ubikadmin
--

COPY public.livres (id, titre, date, auteur_id) FROM stdin;
1	book with tags	2021-09-06 00:00:00	1
2	book with nothing	2021-09-06 00:00:00	1
4	TEST	7711-01-01 00:00:00	3
5	a	1212-12-12 00:00:00	3
6	78	7777-07-07 00:00:00	1
7	opo	1111-01-01 00:00:00	2
8	kk	8998-07-07 00:00:00	2
\.


--
-- Data for Name: tag_livre; Type: TABLE DATA; Schema: public; Owner: ubikadmin
--

COPY public.tag_livre (tag_id, livre_id) FROM stdin;
1	1
2	2
4	2
1	4
5	1
2	4
3	4
4	4
5	4
2	1
3	1
4	1
1	2
3	2
5	2
3	5
2	6
4	7
3	8
4	8
5	8
\.


--
-- Data for Name: tags; Type: TABLE DATA; Schema: public; Owner: ubikadmin
--

COPY public.tags (id, titre) FROM stdin;
1	Python
2	Love
3	Sound
4	Religion
5	Time
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: ubikadmin
--

COPY public.users (id, nom, prenom, login, password) FROM stdin;
\.


--
-- Name: auteurs_id_seq; Type: SEQUENCE SET; Schema: public; Owner: ubikadmin
--

SELECT pg_catalog.setval('public.auteurs_id_seq', 6, true);


--
-- Name: livres_id_seq; Type: SEQUENCE SET; Schema: public; Owner: ubikadmin
--

SELECT pg_catalog.setval('public.livres_id_seq', 8, true);


--
-- Name: tags_id_seq; Type: SEQUENCE SET; Schema: public; Owner: ubikadmin
--

SELECT pg_catalog.setval('public.tags_id_seq', 5, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: ubikadmin
--

SELECT pg_catalog.setval('public.users_id_seq', 1, false);


--
-- Name: auteurs auteurs_pkey; Type: CONSTRAINT; Schema: public; Owner: ubikadmin
--

ALTER TABLE ONLY public.auteurs
    ADD CONSTRAINT auteurs_pkey PRIMARY KEY (id);


--
-- Name: livres livres_pkey; Type: CONSTRAINT; Schema: public; Owner: ubikadmin
--

ALTER TABLE ONLY public.livres
    ADD CONSTRAINT livres_pkey PRIMARY KEY (id);


--
-- Name: tag_livre tag_livre_pkey; Type: CONSTRAINT; Schema: public; Owner: ubikadmin
--

ALTER TABLE ONLY public.tag_livre
    ADD CONSTRAINT tag_livre_pkey PRIMARY KEY (tag_id, livre_id);


--
-- Name: tags tags_pkey; Type: CONSTRAINT; Schema: public; Owner: ubikadmin
--

ALTER TABLE ONLY public.tags
    ADD CONSTRAINT tags_pkey PRIMARY KEY (id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: ubikadmin
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: livres livres_auteur_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: ubikadmin
--

ALTER TABLE ONLY public.livres
    ADD CONSTRAINT livres_auteur_id_fkey FOREIGN KEY (auteur_id) REFERENCES public.auteurs(id);


--
-- Name: tag_livre tag_livre_livre_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: ubikadmin
--

ALTER TABLE ONLY public.tag_livre
    ADD CONSTRAINT tag_livre_livre_id_fkey FOREIGN KEY (livre_id) REFERENCES public.livres(id);


--
-- Name: tag_livre tag_livre_tag_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: ubikadmin
--

ALTER TABLE ONLY public.tag_livre
    ADD CONSTRAINT tag_livre_tag_id_fkey FOREIGN KEY (tag_id) REFERENCES public.tags(id);


--
-- PostgreSQL database dump complete
--

