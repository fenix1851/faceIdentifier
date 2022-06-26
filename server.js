const express = require("express");
const swaggerJsDoc = require('swagger-jsdoc')
const swaggerUi = require("swagger-ui-express");

const app = express();

const swaggerOptions = {
  swaggerDefinition: {
    info: {
      title: 'API',
      version: '1.0.0'
    }
  },
  apis: ['server.js']
}

const storage = multer.memoryStorage();
const upload = multer({ storage });


app.use(express.static("./uploads"));
/**
 * @swagger
 * /:
 *  post:
 *    description: take photo, return compress photo
 *      responces:
 *        200:
 *          description: Succes
 */
app.get("/", (req, res) => {
  return res.json({ message: "ServerWorking" });
});
app.post("/", upload.single("picture"), async (req, res) => {
  fs.access("./uploads", (error) => {
    if (error) {
      fs.mkdirSync("./uploads");
    }
  });
  const { buffer, originalname } = req.file;
  const timestamp = new Date().toISOString();
  const ref = `${timestamp}-${originalname}.webp`;
  await sharp(buffer)
    .webp({ quality: 20 })
    .toFile("./uploads/" + ref);
  const link = `http://localhost:3000/${ref}`;
  return res.json({ link });
});
app.listen(3000);
