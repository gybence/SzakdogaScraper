--
-- PostgreSQL database dump
--

-- Dumped from database version 11.0
-- Dumped by pg_dump version 11.0

-- Started on 2018-11-04 21:32:18

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 199 (class 1259 OID 16426)
-- Name: accepted_sourcesseq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.accepted_sourcesseq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.accepted_sourcesseq OWNER TO postgres;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 198 (class 1259 OID 16421)
-- Name: accepted_sources; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.accepted_sources (
    id numeric(8,0) DEFAULT nextval('public.accepted_sourcesseq'::regclass) NOT NULL,
    url character varying(200) NOT NULL,
    spider character varying(50) NOT NULL,
    inserted time without time zone DEFAULT now()
);


ALTER TABLE public.accepted_sources OWNER TO postgres;

--
-- TOC entry 197 (class 1259 OID 16402)
-- Name: scrapytableseq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.scrapytableseq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.scrapytableseq OWNER TO postgres;

--
-- TOC entry 196 (class 1259 OID 16394)
-- Name: scrapytable; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.scrapytable (
    id numeric(8,0) DEFAULT nextval('public.scrapytableseq'::regclass) NOT NULL,
    url character varying(200) NOT NULL,
    response json,
    inserted timestamp without time zone DEFAULT now(),
    source_id numeric(8,0)
);


ALTER TABLE public.scrapytable OWNER TO postgres;

--
-- TOC entry 2827 (class 0 OID 16421)
-- Dependencies: 198
-- Data for Name: accepted_sources; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.accepted_sources (id, url, spider, inserted) FROM stdin;
4	https://index.hu/	index_spider	19:43:04.563782
5	https://edition.cnn.com/	cnn_spider	19:53:05.483882
6	https://www.cnn.com/	cnn_spider	20:08:26.892781
\.


--
-- TOC entry 2825 (class 0 OID 16394)
-- Dependencies: 196
-- Data for Name: scrapytable; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.scrapytable (id, url, response, inserted, source_id) FROM stdin;
34	https://index.hu/techtud/2018/11/03/kulonos_felhot_figyel_a_mars_express_urszonda/	{"Url": "https://index.hu/techtud/2018/11/03/kulonos_felhot_figyel_a_mars_express_urszonda/", "ContentTitle": "Index - Tech-Tudom\\u00e1ny - K\\u00fcl\\u00f6n\\u00f6s felh\\u0151t figyel a Mars Express \\u0171rszonda", "Title": "K\\u00fcl\\u00f6n\\u00f6s felh\\u0151t figyel a Mars Express \\u0171rszonda", "Author": "Hirek.csillagaszat.hu", "Date": "2018.11.03. 18:43", "RelatedTitles": [{"RelTitle": "Foly\\u00e9kony vizet tal\\u00e1ltak a Marson", "RelDesc": "Olasz kutat\\u00f3k szerint egy 20 kilom\\u00e9ter \\u00e1tm\\u00e9r\\u0151j\\u0171 t\\u00f3 rejt\\u0151zik a Mars d\\u00e9li j\\u00e9gsapk\\u00e1ja alatt.", "RelHref": "https://index.hu/tudomany/2018/07/25/folyekony_viz_mars/"}, {"RelTitle": "A Mars j\\u00e9gspir\\u00e1ljair\\u00f3l adott ki fot\\u00f3kat az ESA", "RelDesc": "Az \\u00e9szaki sarki j\\u00e9gsapka forg\\u00f3szeleknek k\\u00f6sz\\u00f6nheti a jellegzetes alakj\\u00e1t.", "RelHref": "https://index.hu/tudomany/2017/02/03/a_mars_jegspiraljairol_adott_ki_fotokat_az_esa/"}, {"RelTitle": "Megk\\u00fcldte els\\u0151 k\\u00e9peit a Marsr\\u00f3l az orosz-eur\\u00f3pai \\u0171rszonda", "RelDesc": "A kering\\u0151 egys\\u00e9g a bolyg\\u00f3 felsz\\u00edn\\u00e9t\\u0151l alig 250 km-re haladt el a Hebes Chasma r\\u00e9gi\\u00f3 felett.", "RelHref": "https://index.hu/tudomany/2016/11/29/megkuldte_elso_kepeit_a_marsrol_az_orosz-europai_urszonda/"}, {"RelTitle": "Egy m\\u00e1sodperces hiba okozta az \\u0171rszonda veszt\\u00e9t", "RelDesc": "3,7 kilom\\u00e9ter magasan \\u00fagy \\u00e9rz\\u00e9kelte, hogy m\\u00e1r lesz\\u00e1llt, eldobta az erny\\u0151t \\u00e9s le\\u00e1ll\\u00edtotta a rak\\u00e9t\\u00e1kat.", "RelHref": "https://index.hu/tudomany/2016/11/24/elszamolta_a_magassagot_az_europai_mars-szonda/"}], "Lead": null, "ArticleChildren": ["Szeptember 13-a \\u00f3ta k\\u00f6veti az ESA Mars Express szond\\u00e1ja egy hossz\\u00fak\\u00e1s felh\\u0151 fejl\\u0151d\\u00e9s\\u00e9t a bolyg\\u00f3 egyenl\\u00edt\\u0151j\\u00e9hez k\\u00f6zeli, 20 kilom\\u00e9ter magas Arsia Mons vulk\\u00e1n k\\u00f6zel\\u00e9ben. Az elhelyezked\\u00e9se ellen\\u00e9re nem vulk\\u00e1ni aktivit\\u00e1shoz k\\u00f6thet\\u0151, hanem a domborzathoz. Az orografikus vagy lee-felh\\u0151nek is nevezett jelens\\u00e9g gyakori a r\\u00e9gi\\u00f3ban, a vulk\\u00e1ni hegyek \\u00e1ltal k\\u00e9nyszer\\u00edtett fel\\u00e1raml\\u00e1sok, az \\u00fagynevezett orografikus emel\\u00e9s hozza l\\u00e9tre.", "A Mars Express Visual Monitoring Camera (VMC) felv\\u00e9tel\\u00e9n megny\\u00falt, feh\\u00e9r alakzatk\\u00e9nt jelenik meg a felh\\u0151, ami az Arsia Mons vulk\\u00e1nt\\u00f3l nyugatra, 1500 kilom\\u00e9ter hosszan ter\\u00fcl el. (Kontraszt: a k\\u00fap alak\\u00fa vulk\\u00e1n \\u00e1tm\\u00e9r\\u0151je k\\u00f6r\\u00fclbel\\u00fcl 250 kilom\\u00e9ter.)", "N\\u00e9h\\u00e1ny hete, okt\\u00f3ber 16-\\u00e1n volt a Mars \\u00e9szaki f\\u00e9ltek\\u00e9j\\u00e9n a t\\u00e9li napfordul\\u00f3. Az el\\u0151z\\u0151 h\\u00f3napokban az Arsia Mons-hoz hasonl\\u00f3 nagy vulk\\u00e1nok feletti felh\\u0151aktivit\\u00e1s t\\u00f6bbnyire megsz\\u0171nik, m\\u00edg a marsi \\u00e9v t\\u00f6bbi r\\u00e9sz\\u00e9ben a cs\\u00facsok felh\\u0151be burkol\\u00f3znak. Ugyanakkor a vulk\\u00e1n d\\u00e9lnyugati oldal\\u00e1n\\u00e1l meg szokott jelenni az itteni k\\u00e9peken l\\u00e1that\\u00f3hoz hasonl\\u00f3, \\u00e9vszakosan visszat\\u00e9r\\u0151 v\\u00edzj\\u00e9gfelh\\u0151. Kor\\u00e1bban m\\u00e1r 2009-ben, 2012-ben \\u00e9s 2015-ben is megfigyelt hasonl\\u00f3t a Mars Express \\u00e9s m\\u00e1s egys\\u00e9gek is.", "A felh\\u0151 alakja v\\u00e1ltozik egy marsi nap leforg\\u00e1sa alatt. A helyi reggeli \\u00f3r\\u00e1kban n\\u00f6vekszik a vulk\\u00e1non kialakul\\u00f3 buk\\u00f3sz\\u00e9l \\u00e9s a hegyv\\u00f6lgyi sz\\u00e9l hat\\u00e1s\\u00e1ra, majdnem p\\u00e1rhuzamosan az egyenl\\u00edt\\u0151vel. \\u00cdgy akkor\\u00e1ra n\\u0151het, hogy m\\u00e1r f\\u00f6ldi teleszk\\u00f3pokkal is megfigyelhet\\u0151v\\u00e9 v\\u00e1lik.", "A v\\u00edzj\\u00e9gfelh\\u0151k kialakul\\u00e1sa er\\u0151sen f\\u00fcgg a l\\u00e9gk\\u00f6rben jelenlev\\u0151 por mennyis\\u00e9g\\u00e9t\\u0151l. Az ilyen \\u00e9s hasonl\\u00f3 k\\u00e9pekb\\u0151l, melyeket a bolyg\\u00f3t j\\u00faniusban \\u00e9s j\\u00faliusban elnyel\\u0151 hatalmas porvihar ut\\u00e1n k\\u00e9sz\\u00edtettek, sok fontos dolgot tudhatunk meg a por hat\\u00e1s\\u00e1r\\u00f3l a felh\\u0151k fejl\\u0151d\\u00e9s\\u00e9re \\u00e9s az \\u00e9v sor\\u00e1n megfigyelhet\\u0151 v\\u00e1ltoz\\u00e1saikra.", "Id\\u00e9n az Arsia Mons k\\u00f6zel\\u00e9ben lebeg\\u0151 megny\\u00falt felh\\u0151r\\u0151l l\\u00e1that\\u00f3 \\u00e9s k\\u00f6zeli infrav\\u00f6r\\u00f6s tartom\\u00e1nyban is k\\u00e9sz\\u00edtettek felv\\u00e9teleket az OMEGA spektrom\\u00e9terrel, valamint a Mars Express High Resolution Stereo Camera (HRSC) berendez\\u00e9s\\u00e9vel. \\u00cdgy a kutat\\u00f3knak sz\\u00e1mos k\\u00fcl\\u00f6nb\\u00f6z\\u0151 adat \\u00e1ll rendelkez\\u00e9s\\u00e9re a jelens\\u00e9g tanulm\\u00e1nyoz\\u00e1s\\u00e1ra.", "(Csillag\\u00e1szat.hu)"]}	2018-11-03 20:56:16.5417	4
38	https://www.cnn.com/2018/11/02/entertainment/alec-baldwin-arrested/index.html	{"Url": "https://www.cnn.com/2018/11/02/entertainment/alec-baldwin-arrested/index.html", "ContentTitle": null, "Title": "Alec Baldwin arrested, charged with assault in New York - CNN"}	2018-11-03 21:34:59.347896	6
\.


--
-- TOC entry 2834 (class 0 OID 0)
-- Dependencies: 199
-- Name: accepted_sourcesseq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.accepted_sourcesseq', 6, true);


--
-- TOC entry 2835 (class 0 OID 0)
-- Dependencies: 197
-- Name: scrapytableseq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.scrapytableseq', 38, true);


--
-- TOC entry 2700 (class 2606 OID 16425)
-- Name: accepted_sources accepted_sources_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.accepted_sources
    ADD CONSTRAINT accepted_sources_pkey PRIMARY KEY (id);


--
-- TOC entry 2698 (class 2606 OID 16401)
-- Name: scrapytable scrapytable_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.scrapytable
    ADD CONSTRAINT scrapytable_pkey PRIMARY KEY (id);


--
-- TOC entry 2702 (class 2606 OID 16431)
-- Name: accepted_sources unique_url; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.accepted_sources
    ADD CONSTRAINT unique_url UNIQUE (url);


--
-- TOC entry 2696 (class 1259 OID 16441)
-- Name: fki_source_id_const; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fki_source_id_const ON public.scrapytable USING btree (source_id);


--
-- TOC entry 2703 (class 2606 OID 16436)
-- Name: scrapytable source_id_const; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.scrapytable
    ADD CONSTRAINT source_id_const FOREIGN KEY (source_id) REFERENCES public.accepted_sources(id);


-- Completed on 2018-11-04 21:32:19

--
-- PostgreSQL database dump complete
--

