create table if not exists members
(
    name        text    not null,
    index       text    not null,
    email       text    not null,
    user_id     bigint  not null,
    city        text    not null,
    street      text    not null,
    interests   text    not null,
    send        boolean default false not null,
    get         boolean default false not null
);

alter table members
    owner to postgres;
