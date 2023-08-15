#!/usr/bin/node

// concats 2 files

// importing fs module
const fs = require('fs');

// get command line arguments
const [, , firstFile, secondFile, newFile] = process.argv;

// reading file contents
const content1 = fs.readFileSync(firstFile, 'utf-8');
const content2 = fs.readFileSync(secondFile, 'utf-8');

// concatenating the contents
const newContent = content1 + content2;

// writing the content to the new file
fs.writeFileSync(newFile, newContent, 'utf-8');
