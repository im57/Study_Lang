#### Go 언어 소개 및 설치하기

- 키워드 25개 뿐

- GO

  - 변수 정의 해야함

  - 세미콜론을 붙이지 않음

  - 강한 정적 타입 사용

    

#### Hello, World 프로그램 작성하기

- fmt 패키지는 입출력과 관련된 기능을 제공
- 실행
  - go run ''파일이름hello.go'' -> 바로 실행
  - go build ''파일이름hello.go'' -> 컴파일된 프로그램 생성 (./''생성 프로그램hello'' 으로 실행)



#### 변수와 값

- 변수와 값

  - 문자열, 정수, 부동소수점, boolean 등의 기본 값 존재
  - 존재 하지 않는 값을 표현할 때는 nil 이용

  ```go
  var a int = 10
  var a = 10   //타입 추론
  a := 10   //짧은 표현
  fmt.println(a)   //출력
  ```

  - 상수를 선언할 때는 const 키워드를 이용

  - 상수로 선언된 변수는 초기값을 변경 불가

    ```go
    package main
    import "fmt"
    const s string "seoul"
    func main(){
        fmt.println(s)
    	s="busan"   //error
    }
    ```





#### 반복문 (For)

- 반복문

  - while, do while  없음. 오로지 for 구문만 이용

  - 지시자 뒤에 괄호 붙으면 오류

  - for 문에 아무런 조건을 입력하지 않으면 입력값은 true 로 간주

  - break 명령어로 반복 종료

  - continue 명령어로 현재 분기의 코드를 무시하고 다음 반복 주기로 이동

    ```go
    package main
    import "fmt"
    func main(){
        i:=1
        for i <= 10{
            fmt.println(i)
            i =i+1
        }
        //for i:=1; i<=10; i++{} 와 동일
        
        i:=1
        for{
            if i==10{
                break
            }
            if i%2==0{
                continue
            }
            fmt.println(i)
            i++
        }
    }
    ```





#### 조건문 (If/Else)

- 조건문

  ```go
  package main
  import "fmt"
  func main(){
      score:=92
      if score>90{
          fmt.println(score":A+") //92 :A+
      } else if{
          fmt.println(score, ":A0")
      } else{
          fmt.println(score, ":F")
      }
  }
  ```





#### 스위치 구문 (Switch)

- 스위치

  - break 따로 필요없음

  ```go
  package main
  import {
      "fmt"
      "time"
  }
  func main(){
      switch time.Now().Weekday(){
          case time.Saturday:
          	fmt.println("Saturday")
          case time.Sunday:
          	fmt.println("Sunday")
          default:
          fmt.println("Not weekend")
      }
  }
  ```





#### 배열과 슬라이스

- 배열

  - 한 번 집합의 크기를 정하면 변경할 수 없음

  - 배열에는 동일한 타입의 데이만 저장

  - 배열의 원소에 접근할 때는 원소의 인덱스를 0 번부터 시작해서 접근

  - 다차원 배열 가능

    ```go
    package main
    import "fmt"
    func main(){
        var a [5]int
        fmt.println("empty set:", a) //empty set: [0 0 0 0 0]
        
        b:=[3]string{"a","b","c"}  
        fmt.println("b:",b)  //b: [a b c]
        fmt.println("b[0]:"b[0])  //b[0]: a
        
        //다차원 배열
        var c [3][3]
        for i:=0;i<3;i++{
            for j:=0;j<3;j++{
                c[i][j]=i+j
            }
        }
        fmt.println("c[3][3]:",c)  //c[3][3]: [[0 1 2] [1 2 3] [2 3 4]]
    }
    ```



- 슬라이스

  - 집합의 크기를 자유롭게 늘릴 수 있으며, 파이썬 문법과 같이 구간 접근 가능

  - 정의할 때 make 함수 이용

  - 구간접근은 slice[start:end] 로 접근 가능 (start ~ end-1)

    ```go
    package main
    import "fmt"
    func main(){
        a:=make([]int,3)
        a[0]=0
        a[1]=1
        a[2]=2
        
        fmt.print("a:",a) //a: [0 1 2]
        
        a=append(a,"3")  
        fmt.println("a:",a)  //a: [0 1 2 3]
        fmt.println("a[1:3]:",a[1:3])  //a[1:3]: [1 2]
        fmt.println("a[:4]:",a[:4])  //a[:4]: [0 1 2 3]
    }
    ```





#### Maps 와 Range

- Map

  - 정의할 때 make 함수 이용
  - 데이터 접근하는 a[key] 구문은 두 개의 값을 리턴하는데, 두 번째 결과값은 해당 값이 존재하는지 여부

  ```go
  package main
  import "fmt"
  func main(){
      a:=make(map[string]int)  //map[key]value
      a["Tom"]=80
      a["Joe"]=72
      a["Bob"]=65
      
      _,isTom := a["Tom"]  //_에 변수이름 넣고 사용하지 않으면 오류 -> 사용 안 할 때 _ 사용
      fmt.println("is Tom in a?:",isTom)  //is Tom in a?: true
      
      _,isJam := a["Jam"]
      fmt.println("is Jam in a?:",isJam)  //is Jam in a?: false
      
      bobS,isBob := a["Bob"]  //bobS 사용 안 하면 오류
      fmt.println(bobS,"Bob in a?:",isBob)  //65 Bob in a?: true
  }
  ```



- Range

  - 배열 (Array) 혹은 맵 (Map) 데이터 자료구조의 내용을 반복하는 용도로 많이 이용

    ```go
    package main
    import "fmt"
    func main(){
        nums := [5]int{1,2,3,4,5}
        sum:=0
        for _,num:=range nums{
            sum+=num
        }
        fmt.println("sum:",sum)  //sum: 15
        
        
    }
    ```





#### 함수와 포인터

- 함수

  - 함수는 func name(..params ) type { … } 형태로 선언해서 사용

  - 함수의 결과값을 리턴하기 위해서 명시적으로 return 지시자 사용

  - 2 개 이상의 값을 리턴 가능 - 사용 안 하는 변수는 _ 사용 (생략 불가)

  - 익명 함수를 정의 가능

    ```go
    package main
    import "fmt"
    
    func add(a int, b int) int{
        return a+b
    }
    
    func eval(a int, b int)(int, int, int, int){
        return (a+b),(a-b),(a*b),(a/b)
    }
    
    func createSeuence() func() int{
        i:=0
        return func() int{
            i++
            return i
        }
    }
    
    func main(){
        result:=add(1,2)
        fmt.println("1+2",result)
        
        //2 개 이상의 값을 리턴
        add,sub,mul,div:=eval(1,2)  //사용 안 할 때는 _ 사용 - 생략 불가
        fmt.println("1+2",add)
        fmt.println("1-2",sub)
        fmt.println("1*2",mul)
        fmt.println("1/2",div)
        
        //익명 함수
        increment := createSequence()
        fmt.println(increment())  //1
        fmt.println(increment())  //2
        fmt.println(increment())  //3
    
        newInc := createSequence()
        fmt.println(newInc())  //1
    }
    ```



- 포인터

  ```go
  package main
  import "fmt"
  
  func incval(val int){
      val++
  }
  func incptr(val *int){
      *val++
  }
  
  func main(){
      i:=1
      
      incval(i)
      fmt.println("incval:",i)   //1
      
      incptr(&i)
      fmt.println("incval:",i)   //2
  }
  ```

  



#### 구조체와 인터페이스

- 구조체

  - 서로 다른 타입을 가진 필드를 하나의 데이터 타입으로 정의

  - type name struct {fields} 형식

  - 구조체에 메서드 (특정 데이터 타입에 속한 함수) 를 정의 가능

    ```go
    package main
    import "fmt"
    
    type student struct{
        name string
        score int
    }
    
    func main(){
        tom := {"tom", 90}
        bob := student{name:"bob", score:85}
        joe := student{name:"joe"}
        
        fmt.println(tom)  //{tom,90}
        fmt.println(bob)  //{bob,85}
        fmt.println(joe)  //{joe,0}
        
        
    }
    ```

    ```go
    package main
    import "fmt"
    
    type rect struct{
        width int
        height int
    }
    
    func (r rect) area() int{
        return r.width * r.height
    }
    
    func (r rect) minPerfectSquare() rect{
        if r.width>r.height{
            return rect(r.height, r.height)
        } else{
            return rect(r.width, r.width)
        }
    }
    
    func main(){
        r:=rect{20,25}
        
        fmt.println(r.area())  //500
        fmt.println(r.minPerfectSquare())  //{20,20}
    }
    ```

    

- 인터페이스

  - 메서드의 집합을 정의한 타입. 객체지향 언어의 부모 클래스와 동일한 개념
  - 인터페이스의 메서드만 구현된 구조체라면 모두 동일한 인터페이스로 취급할 수 있는데
    이를 덕 타이핑 이라고 부름

  ```go
  package main
  import{
      "fmt"
      "math"
  }
  
  type geometry interface{
      area() float64
  }
  
  type rect struct{
      width, height float64
  }
  type circle struct{
      radius float64
  }
  
  func(r rect) area() float64{
      return r.width * r.height
  }
  
  func(c circle) area() float64{
      return math.Pi * c.radius * c.radius
  }
  
  func measure(g geometry){
      fmt.println(g)
      fmt.println(g.area())
  }
  
  func main(){
      r:=rect{20.0,25.0}
      c:=circle{32.0}
      
      measure(r)
      measure(c)
  }
  
  /*
  {20,25}
  500
  {32}
  3216.9098
  */
  ```

  