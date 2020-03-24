from werkzeug.exceptions import BadRequest, Locked, InternalServerError, Unauthorized


class APIKeyNotSpecifiedError(Unauthorized):
    description = 'No API Key is given'


class NoFileAttachedError(BadRequest):
    description = "No file is attached"


class NoFileSelectedError(BadRequest):
    description = "No file is selected"


class NoFaceFoundError(BadRequest):
    description = "No face is found in the given image"


class OneDimensionalImageIsGivenError(BadRequest):
    description = "Given image has only one dimension"


class MoreThanOneFaceFoundError(BadRequest):
    description = "Found more than one face in the given image"


class ClassifierIsAlreadyTrainingError(Locked):
    description = "Classifier training is already in progress"


class NoTrainedEmbeddingClassifierFound(BadRequest):
    description = "No classifier model is yet trained, please train a classifier first"


class NoFileFoundInDatabaseError(InternalServerError):
    description = 'File is not found in the database'


class InvalidRequestArgumentValueError(BadRequest):
    description = 'Invalid request argument value is given'


class ImageReadLibraryError(BadRequest):
    description = 'Image has incorrect format or is broken'


class FaceHasNoEmbeddingCalculatedError(InternalServerError):
    description = 'Saved face has no embedding calculated and saved in the database'


class NotEnoughUniqueFacesError(BadRequest):
    description = 'Not enough unique faces to start training a new classifier model. ' \
                  'Deleting existing classifiers, if any.'
    exit_code = 5578


EXCEPTIONS_WITH_EXIT_CODES = [NotEnoughUniqueFacesError]
EXIT_CODES = [e.exit_code for e in EXCEPTIONS_WITH_EXIT_CODES]
EXIT_CODE_MAP = {e.exit_code: e for e in EXCEPTIONS_WITH_EXIT_CODES}
