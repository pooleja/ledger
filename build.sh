#!/bin/bash

./acprep update --debug --verbose

cd src
/usr/bin/g++   -g    CMakeFiles/ledger.dir/main.cc.o CMakeFiles/ledger.dir/global.cc.o  -o ../ledger -rdynamic ../libledger.so.3 -lpqxx -lpq -lmpfr -lgmp -ledit -lboost_date_time -lboost_filesystem -lboost_system -lboost_iostreams -lboost_regex -lboost_unit_test_framework -licuuc -Wl,-rpath,/home/ubuntu/ledger::::::::::::

cd ../test/unit
/usr/bin/g++   -g    CMakeFiles/MathTests.dir/t_amount.cc.o CMakeFiles/MathTests.dir/t_commodity.cc.o CMakeFiles/MathTests.dir/t_balance.cc.o CMakeFiles/MathTests.dir/t_expr.cc.o CMakeFiles/MathTests.dir/t_value.cc.o  -o ../../MathTests -rdynamic ../../libledger.so.3 -lpqxx -lpq -lmpfr -lgmp -ledit -lboost_date_time -lboost_filesystem -lboost_system -lboost_iostreams -lboost_regex -lboost_unit_test_framework -licuuc -Wl,-rpath,/home/ubuntu/ledger
/usr/bin/g++   -g    CMakeFiles/UtilTests.dir/t_times.cc.o  -o ../../UtilTests -rdynamic ../../libledger.so.3 -lpqxx -lpq -lmpfr -lgmp -ledit -lboost_date_time -lboost_filesystem -lboost_system -lboost_iostreams -lboost_regex -lboost_unit_test_framework -licuuc -Wl,-rpath,/home/ubuntu/ledger

cd ../..
./acprep update --debug --verbose
