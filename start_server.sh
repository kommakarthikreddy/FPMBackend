# cmd="gunicorn --reload -b :9090 main:app --env NAKED_URL=http://127.0.0.1:9090/"
# echo $cmd
# echo
# echo "Starting Dev Server..."
# $cmd

__PROJECT_DIR__=$(pwd)

run_dev_server() {
    echo "Working dir: $__PROJECT_DIR__"

    echo
    cmd="gunicorn --reload -b :9090 main:app --env NAKED_URL=http://127.0.0.1:9090/"
    echo $cmd
    echo
    echo "Starting Dev Server..."
    echo
    $cmd
}

if [ "$1" == 'setup_db' ]; then
    setup_database
else
    run_dev_server
fi