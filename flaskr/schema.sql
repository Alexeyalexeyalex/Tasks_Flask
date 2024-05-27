use flask;
CREATE TABLE tasks (
  id INTEGER AUTO_INCREMENT,
  title VARCHAR(50) NOT NULL,
  description VARCHAR(50),
  done BOOLEAN NOT NULL,
  created_at DATETIME,
  updated_at DATETIME,
  PRIMARY KEY (id)
);