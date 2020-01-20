INSERT INTO `permission` (`permission_key`, `module`, `label`, `show_in_menu`) VALUES
('add', 'OnePlace\\Skeleton\\Controller\\SkeletonController', 'Add', 0),
('edit', 'OnePlace\\Skeleton\\Controller\\SkeletonController', 'Edit', 0),
('view', 'OnePlace\\Skeleton\\Controller\\SkeletonController', 'View', 0),
('index', 'OnePlace\\Skeleton\\Controller\\SkeletonController', 'Index', 1),
('list', 'OnePlace\\Skeleton\\Controller\\ApiController', 'List', 1);
COMMIT;