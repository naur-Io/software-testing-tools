package org.example;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Disabled;
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

        // adicional wait to load the page
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

    }

    @AfterEach
    void teardown() {
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        driver.quit();

    }

    @Disabled("Teste temporariamente desativado")
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

    @Disabled("Teste temporariamente desativado")
    @Test
    void fiveElevatedToSquare() {
        driver.findElement(By.name("five")).click();
        driver.findElement(By.name("multiply")).click();
        driver.findElement(By.name("five")).click();
        driver.findElement(By.name("calculate")).click();

        WebElement display = driver.findElement(By.id("display"));
        String result = display.getAttribute("value");
        assertEquals("25", result);
    }

    @Disabled("Teste temporariamente desativado")
    @Test
    void square144shouldbe12() {
        driver.findElement(By.name("one")).click();
        driver.findElement(By.name("four")).click();
        driver.findElement(By.name("four")).click();
        driver.findElement(By.name("root2")).click();

        WebElement display = driver.findElement(By.id("display"));
        String result = display.getAttribute("value");
        assertEquals("12", result);
    }

    @Disabled("Teste temporariamente desativado")
    @Test
    void piSquaredShouldBeApprox1_77() {
        driver.findElement(By.name("three")).click();
        driver.findElement(By.name("decimal")).click();
        driver.findElement(By.name("one")).click();
        driver.findElement(By.name("four")).click();
        driver.findElement(By.name("root2")).click();

        WebElement display = driver.findElement(By.id("display"));
        String result = display.getAttribute("value");
        assertEquals("1.7720045147", result);
    }

    @Disabled("Teste temporariamente desativado")
    @Test
    void decimalSum() {
        driver.findElement(By.name("nine")).click();
        driver.findElement(By.name("decimal")).click();
        driver.findElement(By.name("nine")).click();
        driver.findElement(By.name("nine")).click();
        driver.findElement(By.name("add")).click();
        driver.findElement(By.name("zero")).click();
        driver.findElement(By.name("decimal")).click();
        driver.findElement(By.name("zero")).click();
        driver.findElement(By.name("one")).click();
        driver.findElement(By.name("calculate")).click();

        WebElement display = driver.findElement(By.id("display"));
        String result = display.getAttribute("value");
        assertEquals("10", result);
    }

    @Disabled("Teste temporariamente desativado")
    @Test
    void mathExpression() {
        driver.findElement(By.name("four")).click();
        driver.findElement(By.name("add")).click();
        driver.findElement(By.name("eight")).click();
        driver.findElement(By.name("add")).click();
        driver.findElement(By.name("one")).click();
        driver.findElement(By.name("five")).click();
        driver.findElement(By.name("add")).click();
        driver.findElement(By.name("one")).click();
        driver.findElement(By.name("six")).click();
        driver.findElement(By.name("add")).click();
        driver.findElement(By.name("two")).click();
        driver.findElement(By.name("three")).click();
        driver.findElement(By.name("add")).click();
        driver.findElement(By.name("four")).click();
        driver.findElement(By.name("two")).click();
        driver.findElement(By.name("subtract")).click();
        driver.findElement(By.name("three")).click();
        driver.findElement(By.name("seven")).click();
        driver.findElement(By.name("multiply")).click();
        driver.findElement(By.name("two")).click();
        driver.findElement(By.name("calculate")).click();

        WebElement display = driver.findElement(By.id("display"));
        String result = display.getAttribute("value");
        assertEquals("142", result);

    }

    @Test
    void expressionWithParentheses() {
        driver.findElement(By.name("three")).click();
        driver.findElement(By.name("zero")).click();
        driver.findElement(By.name("zero")).click();
        driver.findElement(By.name("divide")).click();
        driver.findElement(By.name("two")).click();
        driver.findElement(By.name("multiply")).click();
        driver.findElement(By.name("five")).click();
        driver.findElement(By.name("calculate")).click();

        WebElement display = driver.findElement(By.id("display"));
        String result = display.getAttribute("value");
        assertEquals("750", result);

    }
}
