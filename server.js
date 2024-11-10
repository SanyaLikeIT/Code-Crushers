const express = require('express');
const multer = require('multer');
const fs = require('fs');
const path = require('path');

const app = express();
const uploadFolder = path.join(__dirname, 'uploads');

if (!fs.existsSync(uploadFolder)) {
  fs.mkdirSync(uploadFolder, { recursive: true });
}

const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, uploadFolder);
  },
  filename: (req, file, cb) => {
    cb(null, Date.now() + '-' + file.originalname);
  }
});

const upload = multer({ storage });

app.use(express.static(path.join(__dirname, 'public')));

app.post('/upload.html/upload', upload.single('file'), (req, res) => {
  if (!req.file) {
    return res.status(400).send('Ошибка: файл не загружен!');
  }
  res.send('Файл успешно загружен и перемещен!');
});

const PORT = process.env.PORT || 3020;
app.listen(PORT, () => {
  console.log(`Сервер запущен на http://localhost:${PORT}`);
});