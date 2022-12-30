set -e

IN=data/fifa21_raw_v2.csv
OUT=data/fifa21_raw_big.csv

cp $IN $OUT

for i in {1..19}
do
    tail -n +2 $IN >> $OUT 
done


