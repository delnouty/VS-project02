import torch
from sentence_transformers import SentenceTransformer

# Загружаем модель
model = SentenceTransformer('all-MiniLM-L6-v2')

# Две текстовые фразы
sentence1 = "Я люблю программирование и изучаю машинное обучение."
sentence2 = "Мне нравится кодить и разбираться в нейросетях."

# Кодируем фразы в векторы
vector1 = torch.tensor(model.encode(sentence1))
vector2 = torch.tensor(model.encode(sentence2))

# Вычисляем косинусное сходство
cos_sim = torch.nn.functional.cosine_similarity(vector1, vector2, dim=0)
cos_distance = 1 - cos_sim  # Преобразование в "расстояние"

# Манхэттенское расстояние (L1)
L1_distance = torch.sum(torch.abs(vector1 - vector2))

# Чебышевская норма (L∞) - максимальная разница
L_infinity = torch.max(torch.abs(vector1 - vector2))

# Взвешенная смешанная метрика
alpha, beta, gamma = 0.5, 0.3, 0.2  # Весовые коэффициенты
hybrid_distance = alpha * cos_distance + beta * L1_distance + gamma * L_infinity

print("🔹 Косинусное расстояние:", cos_distance.item())
print("🔹 Манхэттенское расстояние:", L1_distance.item())
print("🔹 Чебышевская дистанция:", L_infinity.item())
print("🔥 Смешанная метрика:", hybrid_distance.item())
