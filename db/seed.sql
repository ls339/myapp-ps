CREATE TABLE IF NOT EXISTS mytable (
    id SERIAL PRIMARY KEY,
    string_value VARCHAR(255)
);
INSERT INTO mytable(string_value) VALUES ('Hello World');
