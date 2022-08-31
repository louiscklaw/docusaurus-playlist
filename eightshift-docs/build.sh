#!/usr/bin/env bash

set -ex

npm i -d

npm run build

npm run serve
