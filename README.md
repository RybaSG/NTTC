# Nowoczesne techniki transmisji cyfrowej - projekt

## Implementacja wybranych technik przetwarzania w transmisji cyfrowej.
### Standard telewizji cyfrowej [DVB-T2 ETSI EN 302 755](https://www.etsi.org/deliver/etsi_en/302700_302799/302755/01.02.01_40/en_302755v010201o.pdf)

# 1. Cel ćwiczenia
Celem ćwiczenia było napisanie funkcji realizujących operacje rozdzielania wejściowego strumienia
binarnego na podstrumienie bitowe, a następnie przekształcenie tych podstrumieni na bitowe słowa 
(komórki) kodowe (_cell words_) - projekt części nadawczej (demultiplekser).

Dodatkowo należało również zaimplementować operację odwrotną do operacji powyższej - projekt 
częście odbiorczej (multipleksera).

# 2. Autorzy
- Zad2.1N - Dawid Gołębiewski
- Zad2.1O - Dawid Zimończyk
- Zad2.2N - Jakub Duraj
- Zad2.2O - Błażej Wcisło
- Zad2.3N - Aleksander Kędziera
- Zad2.3O - Maciej Ryba
- Zad2.4N - Andreas Gerono
- Zad2.4O - Jacek Gaweł

# 3. Sposób użycia skryptów
## 3.1 Nadajnik
W celu wykorzystania części nadawczej, należy użyć skryptu _nadajniki_marged,py_. W celu prawidłowego
działania skryptu należy przekazać następujące parametry wejściowe:
- Ścieżka dostępu do pliku _*.mat_ zawierającego dane do przetworzenia 
    ```-
    -input_path <input_mat_file_dir>.mat
    ```
- Typ modulacji
    ```
    --modulation [4QAM/QPSK/16QAM/64QAM/256QAM]
    ```
- Wartość N_ldpc
    ```
    --nLdpc [16200/64800]
    ```
- Wartość stopy kodu (parametr opcjonalny)
    ```
    --code_rate [1/2 / 3/4 / 4/5 / 5/6 / 3/5 / 2/3]
    ```
- Ścieżka pliku wyjściowego
    ```
    --output_path <output_mat_file_dir>
    ```
  
Po uruchomieniu skryptu na przykładowych [danych](./mat_test_files) dane otrzymane przez skrypt 
zostaną porównane z danymi znajdującymi się w pliku _*.mat_. Jeżeli dane się zgadzają na konsoli
zostanie zaprezentowana stosowna informacja.

### 3.1.1 Szybkie testowanie
W celu szybkiego przetestowania wszystkich możliwych konfiguracji skryptu dla przygotowanych 
[danych](./mat_test_files) (istotny jest sposób nazywania plików) należy uruchomić skrypt 
_test_files.py_.

Po ukończeniu działania skryptu zostanie utworzony plik _result.txt_, w którym zostaną zaprezentowane
wszystkie użyte konfiguracje komend oraz informacja czy dane zostały prawidłowo zdemultipleksowane.

Jeżeli w trakcie działania skryptu wystąpi różnica pomiędzy danymi, stosowna informacja zostanie 
wyświetlona na konsoli.

## 3.2 Odbiornik
W celu wykorzystania części odbiorczej, należy użyć skryptu _odbiorniki_marged,py_. 
W celu prawidłowego działania skryptu należy wywołać go poprzez linię poleceń w następujący sposób:

```
python3 odbiorniki_meged.py <numer_zadania> <ścieżka_pliku.mat>
```

Gdzie numer zadanie może przyjmować wartości:
- 1.1 - Modulacja QPSK, LDPC = 16200
- 1.2 - Modulacja QPSK, LDPC = 64800
- 1.3 - Modulacja QAM16, LDPC = 64800, stopa kodu = 1/2,3/4,4/5, 5/6 and 2/3
- 1.4 - Modulacja QAM16, LDPC = 16200, stopa kodu = 1/2, 3/4, 4/5, 3/5, 5/6 and 2/3
- 1.5 - Modulacja QAM16, LDPC = 64800, stopa kodu = 3/5
- 2.1 - Modulacja QAM64, LDPC = 64800, stopa kodu = 1/2,3/4,4/5, 5/6 and 2/3
- 2.2 - Modulacja QAM64, LDPC = 16200, stopa kodu = 1/2, 3/4, 4/5, 3/5, 5/6 and 2/3
- 2.3 - Modulacja QAM64, LDPC = 64800, stopa kodu = 3/5
- 3   - Modulacja QAM256, LDPC = 16200
- 4.1 - Modulacja QAM256, LDPC = 64800, stopa kodu = 1/2, 3/4 , 4/5, 5/6
- 4.2 - Modulacja QAM256, LDPC = 64800, stopa kodu = 3/5

Po uruchomieniu skryptu na przykładowych [danych](./mat_test_files) dane otrzymane przez skrypt 
zostaną porównane z danymi znajdującymi się w pliku _*.mat_. Jeżeli dane się zgadzają na konsoli
zostanie zaprezentowana stosowna informacja.
