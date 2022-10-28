# 결측값
## 1. 결측값 다른 값으로 대체하기
### 방법 0)
SELECT IFNULL(col, 'None')
### 방법 1)
SELECT COALESCE(col,'None')
### 방법 2)
SELECT
    CASE WHEN col IS NULL THEN 'None' ELSE col END col

## 2. 해당 열 결측값으로 만들기
SELECT NULL as col

## 3. 결측값 이다/아니다
### 결측값은 value가 아니기 때문에 col = NULL 이런 식으로 처리 못함
WHERE col IS NULL / IS NOT NULL

# 숫자형 처리하기
# 1. float 타입 소수점 반올림
SELECT ROUND(col, 2) as col1

# 날짜값 처리하기
## 1. 형태 바꾸기
SELECT DATE_FORMAT(col, '%Y-%m-%d')

## 2. year, month, day, hour, minute, second
SELECT year(col), month(col), ~~

# str 처리하기
## ex. 강원도로 시작하는 주소 찾기
### 방법 1) - 추천
SELECT col
FROM table
WHERE col LIKE '강원도%'
### 방법 2)
SELECT col
FROM table
WHERE SUBSTRING_INDEX(col, ' ', 1) = '강원도

# 조건문
## HAVING : GROUP BY 한 후 조건문 / WHERE : 그 전 조건문
## 해당 조건 이다/아니다 (= / !=)
WHERE col = 조건
WHERE col != 조건
## BETWEEN : <= 와 같음
WHERE age BETWEEN 20 AND 29
WHERE age >= 20 AND age <= 29
## LIMIT : 상위 n개
### ex. 가장 먼저 들어온 사람 이름 출력
SELECT name
FROM table
ORDER BY date
LIMIT 1
## MAX 값 처리 -> 조건문으로 줘야 한다.
### ex. 가격이 제일 비싼 상품의 정보를 출력 -> MAX는 값일뿐 SELECT로 처리할 수 없음
SELECT *
FROM table
WHERE price = (
SELECT MAX(price)
FROM table)
## 오름차순/내림차순
WHERE col ASC/DESC

# GROUP BY
## GROUP 개수 출력해야 될 때 중복 제거 꼭 생각! - DISTINCT 해야되는지 꼭 생각!
SELECT COUNT(DISTINCT(user_id))
## 각 카테고리 별 max 값 뽑아내기
SELECT category, max_price
FROM A,
SELECT categoray, MAX(price) as max_price
FROM A
GROUP BY cateogry) as B
WHERE A.cateogry = B.category ANd A.price = B.max_price

# [테이블 처리하기]

## UNION : 온라인/오프라인 통합하기 -> 같은 열이름을 가져야 한다.
SELECT col, col1 FROM online
UNION
SELECT col, col1 FROM offline

## JOIN - 1. INNER JOIN : 교집합
FROM A INNER JOIN B ON A.id = B.id

## WITH RECURSIVE : FOR문 재귀로 만들기
### 기본 recursive 템플릿
WITH RECURSIVE table AS (
SELECT 처음 호출하는 쿼리
UNION ALL
SELECT 빈복하는 쿼리 FROM table WHERE 재귀 종료 조건)
SELECT 부모 쿼리
### ex. 시간대별로 들어오는 동물의 수를 출력해라
WITH RECURSIVE hour_tbl AS (
SELECT 0 AS HOUR
UNION ALL
SELECT HOUR+1 FROM hour_tbl WHERE HOUR < 23)
, tmp AS (
SELECT *, HOUR(DATETIME) AS HOUR FROM table)
SELECT h.HOUR, COUNt(t.animal_id)
FROM hour_tble AS h LEFT JOIN tmp AS t ON h.HOUR = t.HOUR
GROUP BY h.HOUR
ORDER BY h.HOUR

## 구간 별로 나누기
### ex. 만원 기준으로 나눠 구간별 상품의 개수를 구하여라
SELECT (
    CASE WHEN price < 10000 THEN 0 ELSE TRUNCATE(price, -4) AS price_group, COUNT(DISTINCT(product_id)))
FROM table
GROUP BY price_group