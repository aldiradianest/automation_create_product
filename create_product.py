import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestCreate_product(unittest.TestCase): 

    @classmethod
    def setUpClass(cls): 
        cls.browser = webdriver.Chrome(ChromeDriverManager().install())
        cls.browser.maximize_window()

    # test case 01 
    def test_case_1_success_create_product(self): # test case
        self.browser.get("http://159.223.80.88:9873/kelontong-store/product_controller")
        time.sleep(1)
        self.browser.find_element(By.ID, "product_name").send_keys("celana chino")
        time.sleep(1)
        self.browser.find_element(By.ID,"product_price").send_keys("50000")
        time.sleep(1)
        self.browser.find_element(By.ID,"product_detail").send_keys("bahan celana")
        time.sleep(1)
        self.browser.find_element(By.ID, "Stock").send_keys("5")
        time.sleep(1)
        self.browser.find_element(By.XPATH,"/html/body/div[2]/form/button").click()
        time.sleep(3)

        # get data 
        validation_message= self.browser.find_element(By.XPATH,"/html/body/div[2]/div/strong").text
        # validasi
        self.assertEqual(validation_message, 'Tambah data berhasil!')
      
    # test case 02
    def test_case_2_Input_product_name_with_empty_or_blank_value(self):
        self.browser.get("http://159.223.80.88:9873/kelontong-store/product_controller")
        time.sleep(1)
        self.browser.find_element(By.ID, "product_name").send_keys("")
        time.sleep(1)
        self.browser.find_element(By.ID,"product_price").send_keys("50000")
        time.sleep(1)
        self.browser.find_element(By.ID,"product_detail").send_keys("bahan celana")
        time.sleep(1)
        self.browser.find_element(By.ID, "Stock").send_keys("5")
        time.sleep(1)
        self.browser.find_element(By.XPATH,"/html/body/div[2]/form/button").click()
        time.sleep(3)

        # get data
        response_message= self.browser.find_element(By.XPATH,"/html/body/div[2]/form/div[1]/span/p").text
        # validasi
        self.assertEqual(response_message, 'Nama produk tidak boleh kosong')

    # test case 03
    def test_case_3_Input_product_name_with_symbol_or_number(self):
        self.browser.get("http://159.223.80.88:9873/kelontong-store/product_controller")
        time.sleep(1)
        self.browser.find_element(By.ID, "product_name").send_keys("Celana chino &^&^&^&8888")
        time.sleep(1)
        self.browser.find_element(By.ID,"product_price").send_keys("50000")
        time.sleep(1)
        self.browser.find_element(By.ID,"product_detail").send_keys("bahan celana")
        time.sleep(1)
        self.browser.find_element(By.ID, "Stock").send_keys("5")
        time.sleep(1)
        self.browser.find_element(By.XPATH,"/html/body/div[2]/form/button").click()
        time.sleep(3)

        # get data
        response_message= self.browser.find_element(By.XPATH,"/html/body/div[2]/form/div[1]/span/p").text
        # validasi
        self.assertEqual(response_message, 'Nama produk tidak valid')

        # test case 04
    def test_case_4_Input_product_price_with_empty_or_blank_value(self):
        self.browser.get("http://159.223.80.88:9873/kelontong-store/product_controller")
        time.sleep(1)
        self.browser.find_element(By.ID, "product_name").send_keys("Celana chino")
        time.sleep(1)
        self.browser.find_element(By.ID,"product_price").send_keys("")
        time.sleep(1)
        self.browser.find_element(By.ID,"product_detail").send_keys("bahan celana")
        time.sleep(1)
        self.browser.find_element(By.ID, "Stock").send_keys("5")
        time.sleep(1)
        self.browser.find_element(By.XPATH,"/html/body/div[2]/form/button").click()
        time.sleep(3)

        # get datas
        response_message= self.browser.find_element(By.XPATH,"/html/body/div[2]/form/div[2]/span/p").text
        # validasi
        self.assertEqual(response_message, 'Harga produk harus diisi')

        # test case 06
    def test_case_6_Input_product_price_with_symbol(self):
        self.browser.get("http://159.223.80.88:9873/kelontong-store/product_controller")
        time.sleep(1)
        self.browser.find_element(By.ID, "product_name").send_keys("Celana chino")
        time.sleep(1)
        self.browser.find_element(By.ID,"product_price").send_keys("!@#$%")
        time.sleep(1)
        self.browser.find_element(By.ID,"product_detail").send_keys("bahan celana")
        time.sleep(1)
        self.browser.find_element(By.ID, "Stock").send_keys("5")
        time.sleep(1)
        self.browser.find_element(By.XPATH,"/html/body/div[2]/form/button").click()
        time.sleep(3)

        # get data
        response_message= self.browser.find_element(By.XPATH,"/html/body/div[2]/form/div[2]/span/p").text
        # validasi
        self.assertEqual(response_message, 'Harga harus diisi dengan Angka')
    
        # test case 07
    def test_case_7_Input_description_product_with_empty_or_blank_value(self):
        self.browser.get("http://159.223.80.88:9873/kelontong-store/product_controller")
        time.sleep(1)
        self.browser.find_element(By.ID, "product_name").send_keys("Celana chino")
        time.sleep(1)
        self.browser.find_element(By.ID,"product_price").send_keys("50000")
        time.sleep(1)
        self.browser.find_element(By.ID,"product_detail").send_keys("")
        time.sleep(1)
        self.browser.find_element(By.ID, "Stock").send_keys("5")
        time.sleep(1)
        self.browser.find_element(By.XPATH,"/html/body/div[2]/form/button").click()
        time.sleep(2)

        # get data
        response_message= self.browser.find_element(By.XPATH,"/html/body/div[2]/form/div[3]/span/p").text
        # validasi
        self.assertEqual(response_message, 'Detail produk tidak boleh kosong')

        # test case 08
    def test_case_8_Input_description_product_with_symbol_or_number(self):
        self.browser.get("http://159.223.80.88:9873/kelontong-store/product_controller")
        time.sleep(1)
        self.browser.find_element(By.ID, "product_name").send_keys("Celana chino")
        time.sleep(1)
        self.browser.find_element(By.ID,"product_price").send_keys("50000")
        time.sleep(1)
        self.browser.find_element(By.ID,"product_detail").send_keys("ajsj78")
        time.sleep(1)
        self.browser.find_element(By.ID, "Stock").send_keys("5")
        time.sleep(1)
        self.browser.find_element(By.XPATH,"/html/body/div[2]/form/button").click()
        time.sleep(2)

        # get data
        response_message= self.browser.find_element(By.XPATH,"/html/body/div[2]/div/strong").text
        # validasi
        self.assertEqual(response_message, 'Tambah data berhasil!')

       # test case 09
    def test_case_9_Input_description_product_with_symbol_and_number(self):
        self.browser.get("http://159.223.80.88:9873/kelontong-store/product_controller")
        time.sleep(1)
        self.browser.find_element(By.ID, "product_name").send_keys("Celana chino")
        time.sleep(1)
        self.browser.find_element(By.ID,"product_price").send_keys("50000")
        time.sleep(1)
        self.browser.find_element(By.ID,"product_detail").send_keys("!!%5666")
        time.sleep(1)
        self.browser.find_element(By.ID, "Stock").send_keys("5")
        time.sleep(1)
        self.browser.find_element(By.XPATH,"/html/body/div[2]/form/button").click()
        time.sleep(2)

        # get data
        response_message= self.browser.find_element(By.XPATH,"/html/body/div[2]/form/div[3]/span/p").text
        # validasi
        self.assertEqual(response_message, 'Produk detail harus diisi dengan huruf')

       # test case 10
    def test_case_10_Input_stock_with_empty_or_blank_value(self):
        self.browser.get("http://159.223.80.88:9873/kelontong-store/product_controller")
        time.sleep(1)
        self.browser.find_element(By.ID, "product_name").send_keys("Celana chino")
        time.sleep(1)
        self.browser.find_element(By.ID,"product_price").send_keys("50000")
        time.sleep(1)
        self.browser.find_element(By.ID,"product_detail").send_keys("bahan ya celana")
        time.sleep(1)
        self.browser.find_element(By.ID, "Stock").send_keys("")
        time.sleep(1)
        self.browser.find_element(By.XPATH,"/html/body/div[2]/form/button").click()
        time.sleep(2)

        # get data
        response_message= self.browser.find_element(By.XPATH,"/html/body/div[2]/form/div[4]/span/p").text
        # validasi
        self.assertEqual(response_message, 'Stok produk tidak boleh kosong')

      # test case 11
    def test_case_11_Input_stock_with_empty_or_blank_value(self):
        self.browser.get("http://159.223.80.88:9873/kelontong-store/product_controller")
        time.sleep(1)
        self.browser.find_element(By.ID, "product_name").send_keys("Celana chino")
        time.sleep(1)
        self.browser.find_element(By.ID,"product_price").send_keys("50000")
        time.sleep(1)
        self.browser.find_element(By.ID,"product_detail").send_keys("bahan ya celana")
        time.sleep(1)
        self.browser.find_element(By.ID, "Stock").send_keys("")
        time.sleep(1)
        self.browser.find_element(By.XPATH,"/html/body/div[2]/form/button").click()
        time.sleep(2)

        # get data
        response_message= self.browser.find_element(By.XPATH,"/html/body/div[2]/form/div[4]/span/p").text
        # validasi
        self.assertEqual(response_message, 'Stok produk tidak boleh kosong')

    @classmethod
    def tearDownClass(cls): # tutup browser
        cls.browser.close() 


if __name__ == "__main__": 
    unittest.main()