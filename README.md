**Автотесты для сайта модерации объявлений**
https://cerulean-praline-8e5aa6.netlify.app/

**Требования:**
- Python 3.7 или выше
- Google Chrome Версия: 146.0.7680.178 (официальная сборка) (64 бит)

**Установить зависимости командой в терминале:**
pip install -r requirements.txt

- Запуск всех тестов: pytest tests -v
- Только тестов главной страницы: pytest tests/test_main_page.py -v
- Только тестов страницы статистики: pytest tests/test_statistics.py -v
- Только мобильной версии: pytest tests/test_mobile_theme.py -v
