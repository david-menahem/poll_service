CREATE TABLE IF NOT EXISTS `question` (
	`id` int AUTO_INCREMENT NOT NULL,
	`title` varchar(255) NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `choice` (
	`id` int AUTO_INCREMENT NOT NULL,
	`question_id` int NOT NULL,
	`choice` varchar(255) NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `answer` (
	`id` int AUTO_INCREMENT NOT NULL,
	`question_id` int NOT NULL,
	`user_id` int NOT NULL,
	`choice_id` int NOT NULL,
	PRIMARY KEY (`id`)
);


ALTER TABLE `choice` ADD CONSTRAINT `choice_fk1` FOREIGN KEY (`question_id`) REFERENCES `question`(`id`);
ALTER TABLE `answer` ADD CONSTRAINT `answer_fk1` FOREIGN KEY (`question_id`) REFERENCES `question`(`id`);

ALTER TABLE `answer` ADD CONSTRAINT `answer_fk3` FOREIGN KEY (`choice_id`) REFERENCES `choice`(`id`);