create table net_io_counters(
    id int auto_increment primary key,
    sent decimal(10,5),
    recv decimal(10,5),
    data datetime
);

select * from net_io_counters;