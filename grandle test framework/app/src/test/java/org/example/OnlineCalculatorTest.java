package org.example;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class OnlineCalculatorTest {

    private WebDriver driver;

    @BeforeEach
    void setup() {
        System.setProperty(
                "webdriver.chrome.driver",
                "C:\\Users\\ruanrlr\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe");
        driver = new ChromeDriver();
        driver.get(" https://www.theonlinecalculator.com");

    }

    @AfterEach
    void teardown() {
        driver.quit();
    }

    @Test
    void testAddition() {
        driver.findElement(By.name("two")).click();
        driver.findElement(By.name("add")).click();
        driver.findElement(By.name("three")).click();
        driver.findElement(By.name("calculate")).click();

        WebElement display = driver.findElement(By.id("display"));
        String result = display.getAttribute("value");

        assertEquals("5", result);
    }

}
