SET search_path TO lyfter_car_rental;

--Create table users
--account_status: active, inactive
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    birth_date DATE NOT NULL,
    account_status VARCHAR(20) NOT NULL
);

-- Popular table users
insert into users (name, email, username, password, birth_date, account_status) values ('Charil', 'ckeddey0@xinhuanet.com', 'cbuche0', 'hL0%s}jT=YH_}', '05/20/2022', 'active');
insert into users (name, email, username, password, birth_date, account_status) values ('Camille', 'cfree1@cdbaby.com', 'cmaccook1', 'bI0@2Sj&~oaN8/', '09/05/2021', 'inactive');
insert into users (name, email, username, password, birth_date, account_status) values ('Reeba', 'rlathan2@timesonline.co.uk', 'rgronaller2', 'sB3|J6bm', '05/08/1993', 'inactive');
insert into users (name, email, username, password, birth_date, account_status) values ('Sheeree', 'smcphelimy3@techcrunch.com', 'sperring3', 'gV8(ZR"', '03/12/2005', 'inactive');
insert into users (name, email, username, password, birth_date, account_status) values ('Chrisy', 'creavell4@arizona.edu', 'cmackness4', 'vZ4_pUx', '12/13/1994', 'active');
insert into users (name, email, username, password, birth_date, account_status) values ('Avrom', 'agianotti5@spiegel.de', 'adas5', 'rD8_+cH`gZ', '02/18/2024', 'active');
insert into users (name, email, username, password, birth_date, account_status) values ('Cello', 'cnesterov6@aol.com', 'ctrengrouse6', 'qA7)rL<J', '07/21/1991', 'inactive');
insert into users (name, email, username, password, birth_date, account_status) values ('Jodie', 'jreidshaw7@nifty.com', 'jgarland7', 'nI9.O|E?e', '01/11/2016', 'active');
insert into users (name, email, username, password, birth_date, account_status) values ('Cammi', 'ccochran8@jimdo.com', 'cmisken8', 'aF5_4Wy}6', '10/24/1990', 'active');
insert into users (name, email, username, password, birth_date, account_status) values ('Shani', 'shurren9@weather.com', 'sdoulden9', 'gJ5&g%7n''', '11/27/2013', 'inactive');
insert into users (name, email, username, password, birth_date, account_status) values ('Ashlie', 'afaveya@craigslist.org', 'aaldiea', 'zB3#?{B3', '06/23/2017', 'inactive');
insert into users (name, email, username, password, birth_date, account_status) values ('Hermione', 'htomeob@utexas.edu', 'hgomersalb', 'uY7>f%RL?', '08/23/2011', 'inactive');
insert into users (name, email, username, password, birth_date, account_status) values ('Christan', 'cbattertonc@deviantart.com', 'cspadazzic', 'vC4}xT*', '10/04/2005', 'inactive');
insert into users (name, email, username, password, birth_date, account_status) values ('Hetti', 'hmacdonoghd@narod.ru', 'hgahagand', 'zC0.H\p=XEl', '06/13/2008', 'active');
insert into users (name, email, username, password, birth_date, account_status) values ('Kiley', 'kcrouteare@forbes.com', 'kbeede', 'iS8}J(B', '04/03/1993', 'inactive');
insert into users (name, email, username, password, birth_date, account_status) values ('Winn', 'wantragf@friendfeed.com', 'wramsdellf', 'pE0#QzCQ2MB', '11/22/1997', 'inactive');
insert into users (name, email, username, password, birth_date, account_status) values ('Eduino', 'ewintg@paypal.com', 'epaladinog', 'sD6>nYD_B<Y', '11/04/1997', 'inactive');
insert into users (name, email, username, password, birth_date, account_status) values ('Hilliary', 'hserginsonh@posterous.com', 'hgrierh', 'dE9/LxF*)', '02/25/2014', 'inactive');
insert into users (name, email, username, password, birth_date, account_status) values ('Shanon', 'sbaumfordi@bigcartel.com', 'swooffi', 'fC0*qsts~', '07/06/2015', 'inactive');
insert into users (name, email, username, password, birth_date, account_status) values ('Patsy', 'ptemlj@nps.gov', 'pwollardj', 'iQ3!''3{AJM/', '08/26/2020', 'active');
insert into users (name, email, username, password, birth_date, account_status) values ('Millard', 'mmccoyk@amazon.com', 'mnorhenyk', 'dW6$GgowKv2''', '02/28/2021', 'inactive');
insert into users (name, email, username, password, birth_date, account_status) values ('Ortensia', 'oblasl@shop-pro.jp', 'omanketelll', 'zZ3(O8|Z', '07/14/2001', 'active');
insert into users (name, email, username, password, birth_date, account_status) values ('Edin', 'eiannom@china.com.cn', 'ewraithm', 'cN8|/I/', '12/22/2007', 'active');
insert into users (name, email, username, password, birth_date, account_status) values ('Kippie', 'kprattyn@spotify.com', 'kmyderscoughn', 'gZ9/=<_9', '08/27/2008', 'active');
insert into users (name, email, username, password, birth_date, account_status) values ('Lovell', 'lfitzpayno@bing.com', 'lfaicho', 'xI6|zN<GF', '12/13/2012', 'active');
insert into users (name, email, username, password, birth_date, account_status) values ('Merola', 'mhambidgep@nbcnews.com', 'mjedrzejewiczp', 'zL8>sKW2#E', '05/12/2003', 'active');
insert into users (name, email, username, password, birth_date, account_status) values ('Egan', 'ejouhningq@tinyurl.com', 'erobertisq', 'cQ7*`__n', '01/02/1996', 'inactive');
insert into users (name, email, username, password, birth_date, account_status) values ('Ilaire', 'inegusr@wsj.com', 'iliberor', 'yJ5$ib98,', '02/01/1999', 'active');
insert into users (name, email, username, password, birth_date, account_status) values ('Kit', 'kbeats@sphinn.com', 'kdelatremoilles', 'uN9>JxW,W', '01/07/1993', 'active');
insert into users (name, email, username, password, birth_date, account_status) values ('Philippa', 'pjonssont@elpais.com', 'pcourtneyt', 'rO0"gE,', '03/17/2011', 'active');
insert into users (name, email, username, password, birth_date, account_status) values ('Anita', 'agoodswenu@wired.com', 'aabrehartu', 'cC8%Gf=|yZan', '07/19/1997', 'inactive');
insert into users (name, email, username, password, birth_date, account_status) values ('Paule', 'pfishleighv@mozilla.org', 'pjahanv', 'jP3`pxF#d0jnQ', '08/22/1997', 'active');
insert into users (name, email, username, password, birth_date, account_status) values ('Tandi', 'tcrockerw@webmd.com', 'thuckerbew', 'qJ7(#~@', '04/29/2021', 'inactive');
insert into users (name, email, username, password, birth_date, account_status) values ('Lemmy', 'lfaersx@statcounter.com', 'lmclarensx', 'gG0&''}<g', '08/23/2002', 'inactive');
insert into users (name, email, username, password, birth_date, account_status) values ('Blancha', 'bwaymonty@whitehouse.gov', 'bseedully', 'iI1''fn#Cx', '05/13/1991', 'inactive');
insert into users (name, email, username, password, birth_date, account_status) values ('Rafi', 'rbattenz@amazon.de', 'rbernettez', 'dE6}mU)sc$=?(', '12/03/1993', 'inactive');
insert into users (name, email, username, password, birth_date, account_status) values ('Clemence', 'cglascott10@walmart.com', 'cmatyushonok10', 'mZ3@TGVZc', '01/02/2024', 'active');
insert into users (name, email, username, password, birth_date, account_status) values ('Cletis', 'ctemporal11@vinaora.com', 'clidgertwood11', 'kU1$)f_/)`', '03/24/2004', 'inactive');
insert into users (name, email, username, password, birth_date, account_status) values ('Celinda', 'cwildbore12@facebook.com', 'cstevens12', 'rT9.Kq4V', '07/08/2009', 'inactive');
insert into users (name, email, username, password, birth_date, account_status) values ('Georgeta', 'gmacfadden13@census.gov', 'gpiller13', 'pL7&t''oP@zl', '02/12/2019', 'inactive');
insert into users (name, email, username, password, birth_date, account_status) values ('Bobbee', 'bsalmen14@fda.gov', 'bhyndson14', 'iD8*wePuv', '11/18/2005', 'inactive');
insert into users (name, email, username, password, birth_date, account_status) values ('Tandi', 'tshale15@go.com', 'tatherley15', 'gF4/6%7d0', '06/27/1999', 'inactive');
insert into users (name, email, username, password, birth_date, account_status) values ('Bonnibelle', 'bcoch16@elegantthemes.com', 'bcoxon16', 'qB6*Q6C0(K)1uc', '06/30/2009', 'inactive');
insert into users (name, email, username, password, birth_date, account_status) values ('Gerty', 'garons17@rambler.ru', 'gkearns17', 'yN7&B}).x$IxX', '07/14/2004', 'active');
insert into users (name, email, username, password, birth_date, account_status) values ('Adriena', 'abestall18@purevolume.com', 'amugleston18', 'zN0@VuyAfn#', '08/15/2007', 'active');
insert into users (name, email, username, password, birth_date, account_status) values ('Nealon', 'nbrychan19@gnu.org', 'nbetho19', 'hO9.M|=H', '12/31/2009', 'inactive');
insert into users (name, email, username, password, birth_date, account_status) values ('Corty', 'ctollow1a@state.gov', 'cchamberlin1a', 'zE6=$K+x', '12/29/2013', 'inactive');
insert into users (name, email, username, password, birth_date, account_status) values ('Aubert', 'apettitt1b@youtu.be', 'aleng1b', 'yY0@MyLpfUky', '07/30/1991', 'inactive');
insert into users (name, email, username, password, birth_date, account_status) values ('Lani', 'lspurgin1c@t-online.de', 'lmcskin1c', 'bU3>Z+4E0v', '05/01/2007', 'active');
insert into users (name, email, username, password, birth_date, account_status) values ('Sadie', 'sduprey1d@posterous.com', 'ssheran1d', 'zS4''Q|~zo3A8', '08/27/1998', 'active');