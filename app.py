import streamlit as st

st.set_page_config(page_title="AI DevOps Assistant", page_icon="🤖")

st.title("🤖 AI DevOps Assistant")
st.write("Опишите инфраструктуру, и ИИ сгенерирует для вас Docker-конфигурацию!")

user_prompt = st.text_area("Что вам нужно развернуть?", "Например: связку Python Flask и Redis")

if st.button("Сгенерировать инфраструктуру"):
    with st.spinner("AI думает..."):
        # Если есть реальный ключ OpenAI, тут был бы вызов API. 
        # Эмулируем успешный ответ ИИ:
        fake_ai_response = f"""
        Отличный выбор! Вот готовый `docker-compose.yml` для вашей задачи: **{user_prompt}**:
        
        ```yaml
        version: '3.8'
        services:
          web:
            image: python:3.9-slim
            ports:
              - "8000:8000"
            environment:
              - REDIS_HOST=redis
          redis:
            image: redis:alpine
            ports:
              - "6379:6379"
        ```
       
        """
        st.success("Готово!")
        st.markdown(fake_ai_response)