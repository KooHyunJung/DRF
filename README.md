# Django REST Framework
Django REST Framework 개인 학습 저장소입니다.

- 간단한 도서 정보 API

- DRF 공식홈페이지(설치방법) : https://www.django-rest-framework.org/

## DRF CBV 기본 ##
### GenericAPIView ###
1) Basic settings
- queryset : 
  - View에서 객체를 반환하는 데 사용해야 하는 쿼리셋. 반드시 1) queryset 속성을 설정하거나, 2) get_queryset() 메서드로 override해서 사용해야 함.
- serializer_class : 
  - 입력된 값을 validate하거나 deserialize하거나, 출력값을 serialize할 때 사용하는 serializer 클래스. 일반적으로 이 속성을 설정하거나 get_serializer_class()메소드로 override해서 사용해야 함
- lookup_field : 
  - 개별 모델 인스턴스의 object 조회를 수행 할 때 사용해야하는 모델 필드. 기본값은 'pk'임. 하이퍼링크 된 API에 custom 값을 사용해야 하는 경우 API views와 serializer 클래스가 lookup필드를 설정해야 함.

![스크린샷 2022-05-17 오후 8 54 34](https://user-images.githubusercontent.com/96563289/168805294-d34597ea-63d9-447e-a573-9c2e96db5e92.png)

![스크린샷 2022-05-17 오후 8 50 11](https://user-images.githubusercontent.com/96563289/168805344-5c625c74-a607-42c1-8eff-74cad17eb9de.png)

## DRF mixins 사용 ##
mixins : https://www.django-rest-framework.org/api-guide/generic-views/#mixins
- APIView와 Mixins의 가장 큰 차이점은 불필요한 코드의 중복을 얼마나 줄일 있는가이다. APIView로 CRUD를 구현해보면 비슷한 논리의 view가 계속해서 반복되는데 이를 CBV 상속을 활용하여 더 간단하게 기능 구현할 수 있다.
- API를 작업할 때 목록을 보여주거나, 생성, 삭제, 수정 등... 이러한 반복적인 기능을 하나의 Mixin 클래스로 제공한다.
  - 장점 : 가독성, 생산성 높아짐
  - 단점 : Mixin 클래스에 존재하는 메소드나 속성을 상속받는 클래스에서 사용할 경우 믹스인 클래스의 메소드가 오버라이딩되어 의도하지 않게 작동할 수 있으니 주의해야한다.

1) ListModelMixin
  - Queryset을 리스팅하는 믹스인
  - .list(request, *args, **kwargs) 메소드로 호출하여 사용
  - GenericAPIView의 self.filter_queryset, self.get_queryset, self.get_serializer 등의 메소드를 활용해 데이터베이스에 저장되어 있는 데이터들을 목록 형태로 response body로 리턴
  - 성공 시, 200 OK response 리턴
2) CreateModelMixin
  - 모델 인스턴스를 생성하고 저장하는 역할을 하는 믹스인
  - .create(request, *args, **kwargs) 메소드로 호출하여 사용
  - 성공 시, 201 Created 리턴
  - 실패 시, 400 Bad Request 리턴
3) RetrieveModelMixin
  - 존재하는 모델 인스턴스를 리턴해 주는 믹스인
  - .retrieve(request, *args, **kwargs) 메소드로 호출하여 사용
  - 성공 시, 200 OK response 리턴
  - 실패 시, 404 Not Found 리턴
4) UpdateModelMixin
  - 모델 인스턴스를 수정하여 저장해 주는 믹스인
  - .update(request, *args, **kwargs) 메소드로 호출하여 사용
  - 부분만 변경하고자 할 경우, .partial_update(request, *args, **kwargs)메소드를 호출하여야 하며, 이 때 요청은 HTTP PATCH requests여야 함
  - 성공 시, 200 OK response 리턴
  - 실패 시, 404 Not Found 리턴
5) DestoryModelMixin
  - 모델 인스턴스를 삭제하는 믹스인
  - .destroy(request, *args, **kwargs) 메소드로 호출하여 사용
  - 성공 시, 204 No Content 리턴
  - 실패 시, 404 Not Found 리턴
  
<img width="1171" alt="스크린샷 2022-05-18 오후 5 56 48" src="https://user-images.githubusercontent.com/96563289/169002326-7340602c-0d81-4740-ba2b-aec21d1b65d4.png">

<img width="992" alt="스크린샷 2022-05-18 오후 5 57 25" src="https://user-images.githubusercontent.com/96563289/169002394-7de3aebc-8c1d-476a-86b9-cfa5d547bbc1.png">

## DRF generics & Viweset & Router ##
앞서 mixins로 코드를 간소화했지만 generics, Viweset & Router 사용하여 더 강력하게 코드 간소화 가능하다.
mixins, generics, Viweset & Route로 인해 점점 코드가 짧아지고 DRF가 대신 만들어주는 기능들이 많아졌다.
개발자 입장에서 할 일이 적어진다는 장점도 있지만, 개발자의 자유도가 낮아진다 보니 커스텀하거나 수정할 때 어려움을 겪을 수 있다. 

따라서 Viweset & Router 가장 강력한 형태라 해서 언제나 답은 아니다. 상황에 따라 적절하게 사용하고 활용할 줄 알아야 최적의 api를 설계할 수 있다 생각한다.

