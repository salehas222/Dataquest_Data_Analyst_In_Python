## 1. Appending ##

/home/dq$ nano beer.txt

## 2. Redirecting from a file ##

/home/dq$ sort beer.txt

## 3. The grep command ##

/home/dq$ grep "bottles of" beer.txt coffee.txt

## 4. Special characters ##

/home/dq$ grep "beer" beer?.txt

## 5. The star wildcard ##

/home/dq$ grep "beer" *.txt

## 6. Piping output ##

/home/dq$ python rand.py | grep 99

## 7. Chaining commands ##

/home/dq$ echo "hi" >> beer.txt && cat beer.txt

## 8. Escaping characters ##

/home/dq$ echo "\"hi again\"" >> beer.txt