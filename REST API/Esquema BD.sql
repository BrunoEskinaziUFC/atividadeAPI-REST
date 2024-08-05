--
-- PostgreSQL database dump
--

-- Dumped from database version 16.3
-- Dumped by pg_dump version 16.3

-- Started on 2024-08-04 23:37:21

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
-- TOC entry 218 (class 1259 OID 16432)
-- Name: Character; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Character" (
    name character varying NOT NULL,
    world integer NOT NULL
);


ALTER TABLE public."Character" OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 16413)
-- Name: DC_Worlds; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."DC_Worlds" (
    "DC_Name" character varying NOT NULL,
    "World_ID" integer NOT NULL
);


ALTER TABLE public."DC_Worlds" OWNER TO postgres;

--
-- TOC entry 215 (class 1259 OID 16399)
-- Name: DataCenters; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."DataCenters" (
    "Name" character varying NOT NULL,
    region character varying,
    worlds integer[]
);


ALTER TABLE public."DataCenters" OWNER TO postgres;

--
-- TOC entry 216 (class 1259 OID 16406)
-- Name: Worlds; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Worlds" (
    id integer NOT NULL,
    name character varying NOT NULL
);


ALTER TABLE public."Worlds" OWNER TO postgres;

--
-- TOC entry 4652 (class 2606 OID 16438)
-- Name: Character Character_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Character"
    ADD CONSTRAINT "Character_pkey" PRIMARY KEY (name, world);


--
-- TOC entry 4650 (class 2606 OID 16419)
-- Name: DC_Worlds DC_Worlds_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."DC_Worlds"
    ADD CONSTRAINT "DC_Worlds_pkey" PRIMARY KEY ("DC_Name", "World_ID");


--
-- TOC entry 4646 (class 2606 OID 16405)
-- Name: DataCenters DataCenters_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."DataCenters"
    ADD CONSTRAINT "DataCenters_pkey" PRIMARY KEY ("Name");


--
-- TOC entry 4648 (class 2606 OID 16412)
-- Name: Worlds Worlds_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Worlds"
    ADD CONSTRAINT "Worlds_pkey" PRIMARY KEY (id);


-- Completed on 2024-08-04 23:37:21

--
-- PostgreSQL database dump complete
--

