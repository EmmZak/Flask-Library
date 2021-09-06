drop table if exists users, livres, auteurs, tags, tag_livre;
drop sequence if exists users_seq, tags_seq, auteurs_seq, livres_seq, tag_livre_seq;

create sequence users_seq start 1 increment 1;
create table users (
	id serial,
	nom varchar(20),
	prenom varchar(20),
	login varchar(20),
	password varchar(20),
	primary key (id)
);

create sequence auteurs_seq start 1 increment 1;
create table auteurs (
	id serial,
	nom varchar(20)  not null,
	prenom varchar(20)  not null,
	primary key (id) 
);

create sequence tags_seq start 1 increment 1;
create table tags (
	id serial,
	lib varchar(50),
	primary key (id)
);

create sequence livres_seq start 1 increment 1;
create table livres (
	id serial,
	titre varchar(50) not null,
	auteur_id int not null,
	date DATE,
	primary key (id),
	foreign key (auteur_id) references auteurs (id) on delete cascade on update cascade
);

