from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer
# Create your views here.

@api_view(['GET','POST'])
def article_get_or_create(request):
    if request.method == 'GET':
        # 전체 게시글 조회
        article = Article.objects.all()

        # 전체 게시글 조회라서, id, title만 보여주고싶음.
        # serializer라는 걸 정의!
        serializer = ArticleListSerializer(article,many = True)
        # 직렬화를 마친 객체의 data만 사용자에게 반환.
        # 그리고, 이 직렬화는 django가 아닌 DRF로 인해 만들어진 것!
        # 즉, 반환도 django 기본 기능이 아니라 DRF의 반환 방식을 쓸 것


        return Response(serializer.data)
    elif request.method == 'POST':
        # 사용자가 보낸 데이터로 article을 생성하고,
        # 그 정보가 유효한지 검증하고,
        # 정상적이면 저장하고
        # 반환한다.
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            # 정상적이면 저장하고
            serializer.save()
            # 반환한다
            return Response(serializer.data)
        return Response(serializer.errors, status=400)