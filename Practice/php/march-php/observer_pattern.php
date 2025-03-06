<?php
interface Observer {
    public function update($message);
}

class User implements Observer {
    public function update($message) {
        echo "Notification: $message\n";
    }
}

class Notifier {
    private $observers = [];
    public function attach(Observer $observer) {
        $this->observers[] = $observer;
    }
    public function notify($message) {
        foreach ($this->observers as $observer) {
            $observer->update($message);
        }
    }
}

$user = new User();
$notifier = new Notifier();
$notifier->attach($user);
$notifier->notify("New event published!");
?>
